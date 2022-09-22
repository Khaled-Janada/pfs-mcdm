from __future__ import annotations

from typing import Iterable, Tuple
import pandas as pd

from .pfn import PFN

pd.set_option('display.float_format', '{:.3f}'.format)


def validate_values(matrix: pd.DataFrame) -> Iterable[Tuple[str, str]]:
    valid = matrix.apply(lambda row: [not x.validate() for x in row])
    indices = valid.apply(lambda x: [(x.name, j) for j in x[x].index], axis=1)
    return sum(indices.tolist(), [])


def prepare_data(array: Iterable[Iterable[(float, float)]], weights: Iterable[float],
                 alts_names: Iterable[str] | None = None) -> (pd.DataFrame, pd.Series):
    df = pd.DataFrame(array).applymap(lambda x: PFN(*x))
    df.index = [f'A{x + 1}' for x in range(df.shape[0])] if alts_names is None else alts_names

    if ind := validate_values(df):
        raise ValueError("Invalid entries in: " + str(ind))

    ws = pd.Series(weights)
    ws = ws / ws.sum()

    if ws.dtype != 'float64':
        raise ValueError("Invalid entries in weights array")

    if ws.shape[0] != df.shape[0]:
        raise ValueError("Length of the weights array must equal the number of criteria")

    return df, ws
