from dataclasses import dataclass
from math import sqrt
from typing import Self


@dataclass
class Vector:
    x: int
    y: int

    def tupled(self) -> tuple[int, int]:
        return self.x, self.y

    def get_distance_of_two_vectors(self, other: Self) -> float:
        return (self - other).length

    @property
    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        if isinstance(other, type(self)):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, int):
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, type(self)):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, int):
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, float):
            return Vector(round(self.x * other), round(self.y * other))


if __name__ == '__main__':
    a = Vector(5, 5)
    b = Vector(1, 1)

    print(a * 1.5)
