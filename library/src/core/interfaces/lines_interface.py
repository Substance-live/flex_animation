from abc import ABC, abstractmethod


# Интерфейс для линии
class ILine(ABC):
    brightness: float

    @abstractmethod
    def calculate_length(self) -> float:
        pass

    @abstractmethod
    def get_start_pos(self) -> list[int]:
        pass

    @abstractmethod
    def get_end_pos(self) -> list[int]:
        pass

# Абстракция для калькулятора яркости
class IBrightnessCalculator(ABC):
    @abstractmethod
    def calculate(self, line: ILine, upper_distance, lower_distance) -> float:
        pass


# Абстракция для стратегии сравнения
class ILineComparisonStrategy(ABC):
    @abstractmethod
    def compare(self, line1: ILine, line2: ILine) -> bool:
        pass
