from math import sqrt
from dataclasses import dataclass


@dataclass
class Circle:
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


@dataclass
class Line:
    first_circle: Circle
    second_circle: Circle
    width: int
    upper_distance: int
    lower_distance: int

    def __lt__(self, other):
        if isinstance(other, Line):
            if self.brightness is None:
                return True
            elif other.brightness is None:
                return False
            else:
                return self.brightness < other.brightness

        raise Exception("Сравнение между не подходящими объектами")

    @property
    def start_pos(self):
        return self.first_circle.pos

    @property
    def end_pos(self):
        return self.second_circle.pos

    @property
    def brightness(self):
        dx = self.second_circle.pos[0] - self.first_circle.pos[0]
        dy = self.second_circle.pos[1] - self.first_circle.pos[1]
        lenght = sqrt(dx ** 2 + dy ** 2)

        if lenght <= self.upper_distance:
            return 1.0
        elif self.upper_distance < lenght <= self.lower_distance:
            return 1 - (lenght - self.upper_distance) / (self.lower_distance - self.upper_distance)
        else:
            return None
