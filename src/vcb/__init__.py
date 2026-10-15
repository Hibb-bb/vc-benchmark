"""vcb: living IRT benchmark for virtual cell models.

Two components share one response-table format (item_id, respondent_id, value):

- A (representation): items are cells (or strata) from a fixed panel; a respondent is an
  embedding; the response is whether a frozen multinomial probe labels the cell correctly.
- B (perturbation): items are (perturbation, context, dose, time) conditions; a respondent
  is a predictor of the post-perturbation pseudobulk; the response is a continuous score
  that is binarized relative to a baseline ladder before the Rasch fit.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RUNS = ROOT / "runs"
