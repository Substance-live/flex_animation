from dataclasses import dataclass

from core.interfaces.objects_interface import IGameObject
from core.models.vector import Vector


@dataclass
class Circle(IGameObject):
    pos: Vector
    direction: Vector
    radius: int
    speed: float

    def move(self):
        self.pos += self.direction * self.speed

    def change_direction(self, coordinate: str):
        if coordinate == 'x':
            self.direction *= -1
            return

        elif coordinate == 'y':
            self.direction *= -1
            return

        raise Exception("Не правильный формат параметра coordinate")

    def get_boundary_offsets(self) -> tuple[int, int]:
        return self.radius, self.radius


@dataclass
class ColoredCircle(Circle):
    color: tuple[int, int, int] = (0, 0, 255)


@dataclass
class Square(IGameObject):
    pos: Vector
    direction: Vector
    side: int
    speed: float

    def move(self):
        self.pos += self.direction * self.speed

    def change_direction(self, coordinate: str):
        if coordinate == 'x':
            self.direction *= -1
        elif coordinate == 'y':
            self.direction *= -1

    def get_boundary_offsets(self) -> tuple[int, int]:
        half_side = self.side // 2
        return half_side, half_side
