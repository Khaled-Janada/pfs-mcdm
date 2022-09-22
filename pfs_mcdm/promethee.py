from __future__ import annotations

import math
from typing import List, Callable, Dict
import pandas as pd

from pfs_mcdm.mcdm import prepare_data


def pref_func_vshape(dist: float, q: float = 0, p: float = 0) -> float:
    if dist <= q:
        return 0
    elif dist > p:
        return 1
    return (dist - q) / (p - q)


def pref_func_ushape(dist: float, q: float = 0) -> float:
    if dist > q:
        return 1
    return 0


def pref_func_level(dist: float, q: float = 0, p: float = 0) -> float:
    if dist <= q:
        return 0
    elif dist > p:
        return 1
    return 0.5


def pref_func_gaussian(dist: float, s: float = 0.5) -> float:
    if dist <= 0:
        return 1 - math.exp(-(dist ** 2) / s ** 2)


def promethee(array: List[List[(float, float)]], weights: List[float], preference_func: str = 'usual',
              alternatives: List[str] | None = None, criteria: List[str] | None = None,
              q: float = 0, p: float = 0, s: float = 0) -> pd.DataFrame:
    matrix = prepare_data(array, alternatives, criteria)
    solution = pd.DataFrame(index=matrix.index.values)

    functions: Dict[str, Callable[[float, ...], float]] = {'vshape': lambda x: pref_func_vshape(x, q, p),
                                                           'usual': pref_func_ushape,
                                                           'gaussian': lambda x: pref_func_gaussian(x, s),
                                                           'ushape': lambda x: pref_func_ushape(x, q),
                                                           'level': lambda x: pref_func_level(x, p)}
    pref_func = functions[preference_func]

    pref_matrix = pd.DataFrame(index=matrix.index.values, columns=matrix.index.values, dtype=float)

    n_alts = matrix.shape[0]
    for i in range(n_alts):
        for j in range(i + 1, n_alts):
            dist = pd.Series.combine(matrix.iloc[i, :], matrix.iloc[j, :], lambda a, b: a.score() - b.score())

            pref_matrix.iat[i, j] = (dist.apply(pref_func) * weights).sum()
            pref_matrix.iat[j, i] = ((-dist).apply(pref_func) * weights).sum()

    solution['Positive Outranking'] = (pref_matrix.sum(axis=1) / (n_alts - 1))
    solution['Negative Outranking'] = (pref_matrix.sum(axis=0) / (n_alts - 1))
    solution['Net Outranking'] = solution['Positive Outranking'] - solution['Negative Outranking']
    solution['Rank'] = solution['Net Outranking'].rank(ascending=False).astype(int)

    return solution
