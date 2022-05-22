# Найти расстояние между двумя точками пространства

from math import sqrt

def distance(x1, y1, x2, y2):
    c = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(c)

distance(-1, 5, -2, 6)
