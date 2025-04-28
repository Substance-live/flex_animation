from abc import ABC, abstractmethod


class IGameObject(ABC):
    pos: list[int]

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
