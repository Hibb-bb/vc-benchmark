"""Frozen probe: one multinomial logistic regression, identical for every embedding.

Train on the train panel's embedding, predict the test panel. The probe is the only
supervised step, and it is held fixed (same C, same iterations, same standardization), so a
difference in responses is a difference in embeddings (PertEval-scFM protocol).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def probe_responses(Z_train, y_train, Z_test, y_test, test_ids, respondent_id: str, C: float = 1.0, max_iter: int = 1000, seed: int = 0) -> pd.DataFrame:
    sc = StandardScaler().fit(Z_train)
    clf = LogisticRegression(C=C, max_iter=max_iter, random_state=seed, n_jobs=-1).fit(sc.transform(Z_train), y_train)
    P = clf.predict_proba(sc.transform(Z_test))
    classes = list(clf.classes_)
    pred = np.array(classes)[P.argmax(1)]
    cls_idx = {c: i for i, c in enumerate(classes)}
    p_true = np.array([P[i, cls_idx[y]] if y in cls_idx else np.nan for i, y in enumerate(y_test)])
    return pd.DataFrame({
        "item_id": test_ids,
        "respondent_id": respondent_id,
        "k": (pred == np.asarray(y_test)).astype(int),
        "n": 1,
        "p_true": p_true,
        "pred": pred,
    })
