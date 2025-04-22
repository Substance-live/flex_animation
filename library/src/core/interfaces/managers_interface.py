from abc import ABC, abstractmethod

from core.interfaces.objects_interface import IGameObject
from core.interfaces.lines_interface import ILine

class MovementHandler(ABC):
    @abstractmethod
    def move(self, circles: list[IGameObject]):
        pass

class LineCreator(ABC):
    @abstractmethod
    def create_line(self, circle1: IGameObject, circle2: IGameObject) -> ILine:
        pass

    @abstractmethod
    def add_line(self, line: ILine):
        pass

    @abstractmethod
    def get_lines(self):
        pass


