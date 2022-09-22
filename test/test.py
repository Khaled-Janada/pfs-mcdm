import pandas as pd

from src.promethee import promethee
from src.simple_aggregation import simple_aggregation
from src.topsis import topsis

# from src import topsis, simple_aggregation, promethee

data = [[(0.9, 0.3), (0.7, 0.6), (0.5, 0.8), (0.6, 0.3)],
        [(0.4, 0.7), (0.9, 0.2), (0.8, 0.1), (0.5, 0.3)],
        [(0.8, 0.4), (0.7, 0.5), (0.6, 0.2), (0.7, 0.4)],
        [(0.7, 0.2), (0.8, 0.2), (0.8, 0.4), (0.6, 0.6)]]

weights = [0.15, 0.25, 0.35, 0.25]

alternatives = ['UNI AIR', 'Transasia', 'Mandarin', 'Daily Air']
criteria = ['Booking', 'Boarding', 'Cabin Service', 'Responsiveness']

agg = simple_aggregation(data, weights, alternatives=alternatives, criteria=criteria)
print("Solution using simple aggregation")
print(agg)

top = topsis(data, weights, alternatives=alternatives, criteria=criteria)
print("\nSolution using TOPSIS")
print(top)

prom = promethee(data, weights, alternatives=alternatives, criteria=criteria, q=0.1, p=0.8, preference_func='vshape')
print(prom)
