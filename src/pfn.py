from __future__ import annotations

from collections import namedtuple
from math import sqrt


class PFN(namedtuple('P', 'u v')):
    u: float
    v: float

    def validate(self) -> bool:
        return (self.u > 0) and (self.v > 0) and (self.u ** 2 + self.v ** 2 <= 1)

    def score(self) -> float:
        return self.u ** 2 - self.v ** 2

    def distance(self, other: PFN) -> float:
        return abs(self.u ** 2 - other.u ** 2) + abs(self.v ** 2 - other.v ** 2) + abs(self.pi ** 2 - other.pi ** 2)

    def round(self, digits: int) -> PFN:
        return PFN(round(self.u, digits), round(self.v, digits))

    @property
    def pi(self) -> float:
        return sqrt(1 - self.u ** 2 - self.v ** 2)

    def __str__(self) -> str:
        return f'P({self.u:.3f}, {self.v:.3f})'

    def __lt__(self, other: PFN) -> bool:
        return self.score() < other.score()

    def __le__(self, other: PFN) -> bool:
        return self.score() <= other.score()

    def __eq__(self, other: PFN) -> bool:
        return self.score() == other.score()

    def __ne__(self, other: PFN) -> bool:
        return self.score() != other.score()

    def __gt__(self, other: PFN) -> bool:
        return self.score() > other.score()

    def __ge__(self, other: PFN) -> bool:
        return self.score() >= other.score()
