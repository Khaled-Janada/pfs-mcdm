from src import topsis, simple_aggregation

t = [[(0.9, 0.3), (0.7, 0.6), (0.5, 0.8), (0.6, 0.3)],
     [(0.4, 0.7), (0.9, 0.2), (0.8, 0.1), (0.5, 0.3)],
     [(0.8, 0.4), (0.7, 0.5), (0.6, 0.2), (0.7, 0.4)],
     [(0.7, 0.2), (0.8, 0.2), (0.8, 0.4), (0.6, 0.6)]]

w = [0.15, 0.25, 0.35, 0.25]

agg = simple_aggregation(t, w, alternatives=['x1', 'x2', 'x3', 'x4'], criteria=['C1', 'C2', 'C3', 'C4'])
print("Solution using simple aggregation")
print(agg)

top = topsis(t, w, alternatives=['x1', 'x2', 'x3', 'x4'], criteria=['C1', 'C2', 'C3', 'C4'])
print("\nSolution using TOPSIS")
print(top)
