# Loaded by STATE inference subprocesses (PYTHONPATH). Our own training checkpoints store a few NumPy scalars
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
