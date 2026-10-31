# Loaded by STATE subprocesses (PYTHONPATH). Our own training checkpoints store a few NumPy scalars
# (e.g. the best validation score); allow exactly those types in torch's weights-only loader instead of
# turning the safe loader off.
try:
    import numpy as np
    import torch
    allowed = [np._core.multiarray.scalar, np.dtype]
    allowed += [getattr(np.dtypes, n) for n in ("Float64DType", "Float32DType", "Int64DType") if hasattr(np, "dtypes") and hasattr(np.dtypes, n)]
    torch.serialization.add_safe_globals(allowed)
except Exception:
    pass

# Faster cell reads for training (only when STATE_NPY_X and STATE_NPY_H5 are set). cell-load fetches one cell at a
# time through h5py, about five small reads plus an attribute lookup per cell; with 2 x 16,384 cells per step that
# Python overhead held training at ~0.15 steps/s with all loader workers at 100% CPU. When the training file's CSR
# arrays are also saved as .npy (memory-mapped, shared by the forked workers), the same row is read from them
# instead. Same cells, same order, same values: only the read changes.
import os as _os
if _os.environ.get("STATE_NPY_X") and _os.environ.get("STATE_NPY_H5"):
    try:
        from pathlib import Path as _Path
        import numpy as _np
        import torch as _torch
        from cell_load.dataset import _perturbation as _pm

        _dir, _h5 = _os.environ["STATE_NPY_X"], str(_Path(_os.environ["STATE_NPY_H5"]).resolve())
        _arrays = {}
        _orig = _pm.PerturbationDataset.fetch_gene_expression

        def _fetch(self, idx):
            if (self.downsample not in (None, 1.0) and self.output_space == "all") or str(_Path(self.h5_path).resolve()) != _h5:
                return _orig(self, idx)
            a = _arrays.get(_os.getpid())
            if a is None:
                a = _arrays[_os.getpid()] = tuple(_np.load(f"{_dir}/{n}.npy", mmap_mode="r") for n in ("indptr", "indices", "data"))
            ptr, ind, dat = a
            s, e = int(ptr[idx]), int(ptr[idx + 1])
            dense = _np.zeros(self.n_genes, dtype=_np.float32)
            dense[ind[s:e]] = dat[s:e]
            return _torch.from_numpy(dense)

        _pm.PerturbationDataset.fetch_gene_expression = _fetch
        print(f"[sitecustomize] cell reads served from {_dir}", flush=True)
    except Exception as _e:
        print(f"[sitecustomize] fast cell reads not enabled: {_e!r}", flush=True)
