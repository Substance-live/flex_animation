from abc import ABC, abstractmethod

from core.interfaces.objects_interface import IGameObject
from core.interfaces.lines_interface import ILine


class LineFactory(ABC):
    @abstractmethod
    def create_line(self, objcet1: IGameObject, objcet2: IGameObject, width: int, upper_distance: int, lower_distance: int) -> ILine:
        pass

class GameObjectFactory(ABC):
    @abstractmethod
    def create(self, pos: list[int], direction: list[int], size: int, speed: float) -> IGameObject:
        pass
