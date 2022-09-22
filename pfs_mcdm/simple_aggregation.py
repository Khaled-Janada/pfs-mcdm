from __future__ import annotations

from typing import List
import pandas as pd

from pfs_mcdm.pfn import PFN
from pfs_mcdm.mcdm import prepare_data


def simple_aggregation(array: List[List[(float, float)]], weights: List[float],
                       alternatives: List[str] | None = None, criteria: List[str] | None = None) -> pd.DataFrame:
    matrix = prepare_data(array, alternatives, criteria)

    solution = pd.DataFrame(index=matrix.index.values)

    def agg_row(row: pd.Series) -> PFN:
        u_sum = sum([x.u * weights[i] for i, x in enumerate(row)])
        v_sum = sum([x.v * weights[i] for i, x in enumerate(row)])
        return PFN(u_sum, v_sum)

    solution['Aggregated'] = matrix.apply(agg_row, axis=1)
    solution['Score'] = solution['Aggregated'].apply(PFN.score)
    solution['Rank'] = solution['Score'].rank(ascending=False).astype(int)

    styler = solution.style
    styler.set_caption("Simple Aggregation")
    styler.format(formatter={'Aggregated': lambda x: "$ {:,.1f}".format(x * -1e6)})

    return solution
