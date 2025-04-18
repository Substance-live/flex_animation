
from dataclasses import dataclass


@dataclass
class Circle:
    pos: list[int, int]
    direction: list[int, int]
    color: int
    speed: int = 1.0


@dataclass
class Tether:
    obj: list[Circle, Circle]


if __name__ == '__main__':
    pass
