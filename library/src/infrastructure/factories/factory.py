from core.interfaces.factories_interface import GameObjectFactory, LineFactory
from core.interfaces.lines_interface import ILine, IBrightnessCalculator, ILineComparisonStrategy
from core.interfaces.objects_interface import IGameObject
from core.models.vector import Vector
from infrastructure.lines.line import StraightLine
from infrastructure.models.model import Circle, Square, ColoredCircle


class CircleFactory(GameObjectFactory):
    def create(self, pos: Vector, direction: Vector, radius: int, speed: float) -> IGameObject:
        return Circle(pos, direction, radius, speed)


class SquareFactory(GameObjectFactory):
    def create(self, pos: Vector, direction: Vector, side: int, speed: float) -> IGameObject:
        return Square(pos, direction, side, speed)


class ColoredCircleFactory(GameObjectFactory):
    def create(self, pos: Vector, direction: Vector, radius: int, speed: float) -> IGameObject:
        return ColoredCircle(pos, direction, radius, speed)


class DefaultLineFactory(LineFactory):
    def __init__(self, brightness_calculator: IBrightnessCalculator, comparison_strategy: ILineComparisonStrategy):
        self.brightness_calculator = brightness_calculator
        self.comparison_strategy = comparison_strategy

    def create_line(self, circle1: IGameObject, circle2: IGameObject, width: int, upper_distance: int,
                    lower_distance: int) -> ILine:
        return StraightLine(circle1, circle2, width, upper_distance, lower_distance, self.brightness_calculator,
                            self.comparison_strategy)
