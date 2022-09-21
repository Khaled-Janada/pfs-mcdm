from __future__ import annotations

from typing import List, Tuple
import pandas as pd

from src.pfn import PFN

pd.set_option('display.float_format', '{:.3f}'.format)


def normalize(vector: List[float]):
    s = sum(vector)
    return [(x / s) for x in vector]


def validate_values(matrix: pd.DataFrame) -> List[Tuple[str, str]]:
    valid = matrix.apply(lambda row: [not x.validate() for x in row])
    indices = valid.apply(lambda x: [(x.name, j) for j in x[x].index], axis=1)
    return sum(indices.tolist(), [])


def prepare_data(array: List[List[(float, float)]],
                 alts_names: List[str] | None = None, crit_names: List[str] | None = None):
    df = pd.DataFrame(array).applymap(lambda x: PFN(*x))

    alts_names = [f'A{x + 1}' for x in range(df.shape[0])] if alts_names is None else alts_names
    df.set_axis(alts_names, axis=0, inplace=True)

    crit_names = [f'C{x + 1}' for x in range(df.shape[1])] if crit_names is None else crit_names
    df.set_axis(crit_names, axis=1, inplace=True)

    if ind := validate_values(df):
        raise ValueError("Invalid entries in: " + str(ind))

    return df
