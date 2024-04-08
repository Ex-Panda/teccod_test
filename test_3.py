import math
from typing import Tuple


class Point:

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def coords(self):
        return self._x, self._y

    @coords.setter
    def coords(self, coordinate: Tuple):
        self._x = coordinate[0]
        self._y = coordinate[1]

    def dist(self, x1: int, y1: int) -> float:
        """Вычисляет расстояние до другой точки"""
        return math.hypot(self._x - x1, self._y - y1)


p1 = Point(1, 2)
print(p1.dist(5, 8))
print(p1.coords)
p1.coords = (3, 7)
print(p1.coords)



