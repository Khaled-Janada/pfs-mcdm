from __future__ import annotations

from typing import List

import pandas as pd

from src.pfn import PFN
from src.mcdm import prepare_data


def topsis(array: List[List[(float, float)]], weights: List[float],
           alternatives: List[str] | None = None, criteria: List[str] | None = None) -> pd.DataFrame:
    matrix = prepare_data(array, alternatives, criteria)

    solution = pd.DataFrame(index=matrix.index.values)

    x_p = matrix.max(axis=0, numeric_only=False)
    x_n = matrix.min(axis=0, numeric_only=False)

    def calc_dist(row: pd.Series) -> pd.Series:
        s = pd.Series(index=['D+', 'D-'], dtype=float)
        s[0] = 0.5 * (row.combine(x_p, func=lambda x, y: PFN.distance(x, y)) * weights).sum()
        s[1] = 0.5 * (row.combine(x_n, func=lambda x, y: PFN.distance(x, y)) * weights).sum()
        return s

    distances = matrix.apply(calc_dist, axis=1)
    solution['D+'] = distances['D+']
    solution['D-'] = distances['D-']

    d_n_max = distances['D-'].max()
    d_p_min = distances['D+'].min()

    solution['Revised Closeness'] = pd.Series.combine(distances['D-'], distances['D+'], func=lambda n, p: (n / d_n_max) - (p / d_p_min))
    solution['Rank'] = solution['Revised Closeness'].rank(ascending=False).astype(int)

    return solution
