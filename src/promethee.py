from __future__ import annotations

from typing import List

import pandas as pd

from src.mcdm import prepare_data


def promethee(array: List[List[(float, float)]], weights: List[float],
              alternatives: List[str] | None = None, criteria: List[str] | None = None) -> pd.DataFrame:
    matrix = prepare_data(array, alternatives, criteria)
    solution = pd.DataFrame(index=matrix.index.values)
    return solution
