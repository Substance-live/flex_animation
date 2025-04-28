from abc import ABC, abstractmethod

from core.models.vector import Vector


class IGameObject(ABC):
    pos: Vector
    direction: Vector

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def change_direction(self, coordinate: str):
        pass

    @abstractmethod
    def get_boundary_offsets(self) -> tuple[int, int]:
        """
        Возвращает смещения (offset_x, offset_y) от позиции до края объекта
        например: для круга это (радиус, радиус)
                  для квадрата (половина стороны, половина стороны)
        """
        pass
