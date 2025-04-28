from dataclasses import dataclass

from core.interfaces.lines_interface import ILine, IBrightnessCalculator, ILineComparisonStrategy
from core.interfaces.objects_interface import IGameObject


@dataclass
class StraightLine(ILine):
    first_circle: IGameObject
    second_circle: IGameObject
    width: int
    upper_distance: int
    lower_distance: int
    brightness_calculator: IBrightnessCalculator
    comparison_strategy: ILineComparisonStrategy

    def __lt__(self, other):
        if isinstance(other, ILine):
            return self.comparison_strategy.compare(self, other)
        raise Exception("Сравнение между не подходящими объектами")

    @property
    def brightness(self):
        return self.brightness_calculator.calculate(self, self.upper_distance, self.lower_distance)

    def calculate_length(self) -> float:
        return self.first_circle.pos.get_distance_of_two_vectors(self.second_circle.pos)

    def get_start_pos(self):
        return self.first_circle.pos

    def get_end_pos(self):
        return self.second_circle.pos


# Стандартный калькулятор яркости
class DefaultBrightnessCalculator(IBrightnessCalculator):
    def calculate(self, line: ILine, upper_distance, lower_distance) -> float:
        length = line.calculate_length()

        if length <= upper_distance:
            return 1.0
        elif upper_distance < length <= lower_distance:
            return 1 - (length - upper_distance) / (lower_distance - upper_distance)
        else:
            return None


# Стандартная стратегия сравнения по яркости
class BrightnessComparisonStrategy(ILineComparisonStrategy):
    def compare(self, line1: ILine, line2: ILine) -> bool:
        if line1.brightness is None and line2.brightness is None:
            return False  # Оба равны None, считаем их одинаковыми
        elif line1.brightness is None:
            return True  # Если яркость первой линии None, она считается меньшей
        elif line2.brightness is None:
            return False  # Если яркость второй линии None, она считается меньшей
        return line1.brightness < line2.brightness  # Стандартное сравнение яркости
