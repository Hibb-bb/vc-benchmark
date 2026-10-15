"""scGen (Lotfollahi et al. 2019) re-implemented in plain torch.

Architecture and rule follow the original: a VAE on log-normalized expression (MSE
reconstruction), encoder and decoder of two 800-unit layers, latent 100, dropout 0.2, KL
weight 5e-5. Prediction for a held-out (perturbation p, context c):

    delta = mean z(cells with p, in training contexts) - mean z(control cells in those
            same contexts, equal count per context)
    predicted cells = decode(z(control cells of c) + delta)

The benchmark response is the pseudobulk delta: mean(predicted) - mean(control of c).
The model sees the benchmark's 2,000 HVGs; other genes fall back to mean_shift so that
all-gene metrics are defined (the pass rule uses the HVG metrics).

Only the unseen-context scheme is possible: a perturbation never seen in any context has
no latent delta.
"""
from __future__ import annotations

import numpy as np
import scipy.sparse as sp
import torch
import torch.nn as nn
import torch.nn.functional as F


def lognorm(X: sp.csr_matrix) -> sp.csr_matrix:
    X = sp.csr_matrix(X, dtype=np.float32)
    tot = np.asarray(X.sum(1)).ravel()
    tot[tot == 0] = 1
    X = sp.diags((1e4 / tot).astype(np.float32)) @ X
    X.data = np.log1p(X.data)
    return X


class VAE(nn.Module):
    def __init__(self, n_in, n_hidden=800, n_latent=100, dropout=0.2):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(n_in, n_hidden), nn.BatchNorm1d(n_hidden), nn.LeakyReLU(), nn.Dropout(dropout),
                                 nn.Linear(n_hidden, n_hidden), nn.BatchNorm1d(n_hidden), nn.LeakyReLU(), nn.Dropout(dropout))
        self.mu = nn.Linear(n_hidden, n_latent)
        self.logvar = nn.Linear(n_hidden, n_latent)
        self.dec = nn.Sequential(nn.Linear(n_latent, n_hidden), nn.BatchNorm1d(n_hidden), nn.LeakyReLU(), nn.Dropout(dropout),
                                 nn.Linear(n_hidden, n_hidden), nn.BatchNorm1d(n_hidden), nn.LeakyReLU(), nn.Dropout(dropout),
                                 nn.Linear(n_hidden, n_in))

    def encode(self, x):
        h = self.enc(x)
        return self.mu(h), self.logvar(h)

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = mu + torch.randn_like(mu) * torch.exp(0.5 * logvar)
        return self.dec(z), mu, logvar


class SCGEN:
    def __init__(self, n_latent=100, n_hidden=800, kl_weight=5e-5, lr=1e-3, batch_size=256, max_epochs=100, patience=10, seed=0, device=None):
        self.cfg = dict(n_latent=n_latent, n_hidden=n_hidden, kl_weight=kl_weight, lr=lr, batch_size=batch_size, max_epochs=max_epochs, patience=patience, seed=seed)
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

    def fit(self, X: np.ndarray, log=print):
        torch.manual_seed(self.cfg["seed"])
        rng = np.random.default_rng(self.cfg["seed"])
        n = X.shape[0]
        val = rng.random(n) < 0.1
        Xt = torch.tensor(X, dtype=torch.float32)
        self.model = VAE(X.shape[1], self.cfg["n_hidden"], self.cfg["n_latent"]).to(self.device)
        opt = torch.optim.Adam(self.model.parameters(), lr=self.cfg["lr"], weight_decay=0)
        tr_idx, va_idx = np.where(~val)[0], np.where(val)[0]
        best, bad, best_state = np.inf, 0, None
        bs = self.cfg["batch_size"]
        for ep in range(self.cfg["max_epochs"]):
            self.model.train()
            perm = rng.permutation(tr_idx)
            tot = 0.0
            for i in range(0, len(perm), bs):
                xb = Xt[perm[i:i + bs]].to(self.device)
                if xb.shape[0] < 2:
                    continue
                rec, mu, logvar = self.model(xb)
                recon = F.mse_loss(rec, xb, reduction="sum") / xb.shape[0]
                kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp()) / xb.shape[0]
                loss = recon + self.cfg["kl_weight"] * kl
                opt.zero_grad()
                loss.backward()
                opt.step()
                tot += loss.item() * xb.shape[0]
            vl = self._val_loss(Xt[va_idx])
            log(f"    epoch {ep+1:3d} train {tot/len(tr_idx):.3f} val {vl:.3f}")
            if vl < best - 1e-3:
                best, bad, best_state = vl, 0, {k: v.detach().clone() for k, v in self.model.state_dict().items()}
            else:
                bad += 1
                if bad >= self.cfg["patience"]:
                    break
        self.model.load_state_dict(best_state)
        self.model.eval()
        return self

    @torch.no_grad()
    def _val_loss(self, Xv):
        self.model.eval()
        tot = 0.0
        for i in range(0, Xv.shape[0], 2048):
            xb = Xv[i:i + 2048].to(self.device)
            if xb.shape[0] < 2:
                continue
            rec, mu, logvar = self.model(xb)
            tot += (F.mse_loss(rec, xb, reduction="sum") + self.cfg["kl_weight"] * -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())).item()
        return tot / max(Xv.shape[0], 1)

    @torch.no_grad()
    def encode(self, X):
        self.model.eval()
        out = []
        for i in range(0, X.shape[0], 4096):
            mu, _ = self.model.encode(torch.tensor(X[i:i + 4096], dtype=torch.float32).to(self.device))
            out.append(mu.cpu().numpy())
        return np.concatenate(out)

    @torch.no_grad()
    def decode(self, Z):
        self.model.eval()
        out = []
        for i in range(0, Z.shape[0], 4096):
            out.append(self.model.dec(torch.tensor(Z[i:i + 4096], dtype=torch.float32).to(self.device)).cpu().numpy())
        return np.concatenate(out)

    def predict_delta(self, Z_pert_by_ctx: dict, Z_ctrl_by_ctx: dict, target_ctx: str, rng=None):
        """Latent arithmetic. Z_pert_by_ctx: {ctx: latent of perturbed cells in a *training* context};
        Z_ctrl_by_ctx: {ctx: latent of control cells}. Returns predicted cells (gene space) for target_ctx."""
        rng = rng or np.random.default_rng(0)
        zp, zc = [], []
        for ctx, Zp in Z_pert_by_ctx.items():
            Zc = Z_ctrl_by_ctx[ctx]
            m = min(len(Zp), len(Zc))
            zp.append(Zp[rng.choice(len(Zp), m, replace=False)])
            zc.append(Zc[rng.choice(len(Zc), m, replace=False)])
        delta = np.concatenate(zp).mean(0) - np.concatenate(zc).mean(0)
        return self.decode(Z_ctrl_by_ctx[target_ctx] + delta)
