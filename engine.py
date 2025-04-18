from models import Circle, Line
import random, math
from random import randint


class Engine:

    def __init__(self, size_window: list[int], count_obj: int):
        self.screen = size_window

        self.circles: list[Circle] = []
        self.lines: list[Line] = []

        for _ in range(count_obj):
            circle = self.get_rand_circle(radius=15, start_speed=1.65)
            self.link_circle(circle)
            self.circles.append(circle)

    def link_circle(self, new_circle):
        for exist_circle in self.circles:
            self.lines.append(Line(first_circle=new_circle, second_circle=exist_circle, width=10, upper_distance=50, lower_distance=250))

    def get_rand_circle(self, radius: int, start_speed: float) -> Circle:
        angle = random.uniform(0, 2 * math.pi)
        dx = round(math.cos(angle) * start_speed)
        dy = round(math.sin(angle) * start_speed)

        return Circle([randint(radius, self.screen[0] - radius), randint(radius, self.screen[1] - radius)],
                      [dx, dy],
                      radius,
                      start_speed)

    def move_figures(self):
        for circle in self.circles:
            circle.move()

            if not circle.radius < circle.pos[0] < self.screen[0] - circle.radius:
                circle.change_direction('x')

            elif not circle.radius < circle.pos[1] < self.screen[1] - circle.radius:
                circle.change_direction('y')
