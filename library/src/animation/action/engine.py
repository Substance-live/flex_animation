import random, math

from random import randint
from dataclasses import dataclass

from animation.logic.models import Circle, Line


@dataclass
class EngineConfig:
    count_obj: int
    circle_radius: int
    start_speed: float
    width_of_line: int
    upper_limit: int
    lower_limit: int

class Engine:

    def __init__(self, size_window: tuple[int, int], config: EngineConfig):
        self.screen = size_window
        self.config = config

        self.circles: list[Circle] = []
        self.lines: list[Line] = []

        for _ in range(config.count_obj):
            circle = self.get_rand_circle(self.config.circle_radius, self.config.start_speed)
            self.link_circle(circle)
            self.circles.append(circle)

    def link_circle(self, new_circle):
        for exist_circle in self.circles:
            self.lines.append(
                Line(new_circle, exist_circle,
                     self.config.width_of_line,
                     self.config.upper_limit, self.config.lower_limit))


    def get_rand_circle(self, radius: int, speed: float) -> Circle:
        angle = random.uniform(0, 2 * math.pi)
        dx = round(math.cos(angle) * speed)
        dy = round(math.sin(angle) * speed)

        return Circle([randint(radius, self.screen[0] - radius), randint(radius, self.screen[1] - radius)],
                      [dx, dy],
                      radius,
                      speed)

    def move_figures(self):
        for circle in self.circles:
            circle.move()

            if not circle.radius < circle.pos[0] < self.screen[0] - circle.radius:
                circle.change_direction('x')

            elif not circle.radius < circle.pos[1] < self.screen[1] - circle.radius:
                circle.change_direction('y')

        self.lines.sort()
