from __future__ import annotations

import json
import numpy as np

# The frozen verifier contains numpy scalar booleans in its decision payload.
# Keep the experiment itself unchanged and make JSON serialization robust here.
_original_dumps = json.dumps


def _default(value):
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def _dumps(obj, *args, **kwargs):
    kwargs.setdefault("default", _default)
    return _original_dumps(obj, *args, **kwargs)


json.dumps = _dumps

from experiments.phase10b_ensemble_verify import main  # noqa: E402


if __name__ == "__main__":
    main()
