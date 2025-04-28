import random
from math import pi, cos, sin

from core.interfaces.factories_interface import LineFactory, GameObjectFactory
from core.interfaces.lines_interface import ILine
from core.interfaces.managers_interface import MovementHandler, LineCreator
from core.interfaces.objects_interface import IGameObject
from core.models.vector import Vector


class GameObjectManager:
    def __init__(self, screen_size: tuple[int, int], obj_size: int, start_speed: float, factory: GameObjectFactory):
        self.screen_size = screen_size
        self.obj_size = obj_size
        self.start_speed = start_speed
        self.factory = factory
        self.objects = []

    def create_random_object(self) -> IGameObject:
        """Создает объект случайным образом в пределах экрана"""
        angle = random.uniform(0, 2 * pi)
        dx = round(cos(angle) * self.start_speed)
        dy = round(sin(angle) * self.start_speed)
        # Используем фабрику для создания объекта
        return self.factory.create(
            Vector(random.randint(self.obj_size, self.screen_size[0] - self.obj_size),
                   random.randint(self.obj_size, self.screen_size[1] - self.obj_size)),
            Vector(dx, dy),
            self.obj_size,
            self.start_speed
        )

    def add_object(self, obj: IGameObject):
        """Добавляет объект в список объектов"""
        self.objects.append(obj)

    def get_object(self):
        """Возвращает список объектов"""
        return self.objects

    def get_objects_from_circle(self, center: Vector, radius: int) -> list[IGameObject]:
        ret = []
        for obj in self.objects:
            if radius >= center.get_distance_of_two_vectors(obj.pos):
                ret.append(obj)

        return ret


class MovementManager(MovementHandler):
    def __init__(self, screen_size: tuple[int, int]):
        self.screen_size = screen_size

    def move(self, objects: list[IGameObject]):
        for obj in objects:
            obj.move()
            offset_x, offset_y = obj.get_boundary_offsets()

            if not offset_x < obj.pos.x < self.screen_size[0] - offset_x:
                obj.change_direction('x')

            if not offset_y < obj.pos.y < self.screen_size[1] - offset_y:
                obj.change_direction('y')


class LineManager(LineCreator):
    def __init__(self, upper_limit: int, lower_limit: int, width_of_line: int, line_factory: LineFactory):
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.width_of_line = width_of_line
        self.line_factory = line_factory
        self.lines = []

    def create_line(self, circle1: IGameObject, circle2: IGameObject) -> ILine:
        return self.line_factory.create_line(circle1, circle2, self.width_of_line, self.upper_limit, self.lower_limit)

    def add_line(self, line: ILine):
        self.lines.append(line)

    def get_lines(self):
        return self.lines
