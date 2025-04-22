from dataclasses import dataclass

from core.interfaces.objects_interface import IGameObject

@dataclass
class Circle(IGameObject):
    pos: list[int]
    direction: list[int]
    radius: int
    speed: float

    def move(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed

    def change_direction(self, coordinate: str):
        if coordinate == 'x':
            self.direction[0] *= -1
            return

        elif coordinate == 'y':
            self.direction[1] *= -1
            return

        raise Exception("Не правильный формат параметра coordinate")

    def get_boundary_offsets(self) -> tuple[int, int]:
        return self.radius, self.radius

@dataclass
class Square(IGameObject):
    pos: list[int]
    direction: list[int]
    side: int
    speed: float

    def move(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed

    def change_direction(self, coordinate: str):
        if coordinate == 'x':
            self.direction[0] *= -1
        elif coordinate == 'y':
            self.direction[1] *= -1

    def get_boundary_offsets(self) -> tuple[int, int]:
        half_side = self.side // 2
        return half_side, half_side

