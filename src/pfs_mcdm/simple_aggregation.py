from __future__ import annotations

from typing import Iterable
import pandas as pd

from .pfn import PFN
from .mcdm import prepare_data


def simple_aggregation(array: Iterable[Iterable[(float, float)]], weights_array: Iterable[float],
                       alternatives: Iterable[str] | None = None) -> pd.DataFrame:
    matrix, weights = prepare_data(array, weights_array, alternatives)
    solution = pd.DataFrame(index=matrix.index.values)

    def agg_row(row: pd.Series) -> PFN:
        u_sum = sum([x.u * weights[i] for i, x in enumerate(row)])
        v_sum = sum([x.v * weights[i] for i, x in enumerate(row)])
        return PFN(u_sum, v_sum)

    solution['Aggregated'] = matrix.apply(agg_row, axis=1)
    solution['Score'] = solution['Aggregated'].apply(PFN.score)
    solution['Rank'] = solution['Score'].rank(ascending=False).astype(int)

    return solution
