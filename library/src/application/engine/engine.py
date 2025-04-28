from application.managers.manager import GameObjectManager
from core.interfaces.managers_interface import MovementHandler, LineCreator
from core.models.vector import Vector


class Engine:
    def __init__(self, size_window: tuple[int, int], count_obj: int, object_manager: GameObjectManager,
                 line_manager: LineCreator, movement_manager: MovementHandler):
        self.screen = size_window
        self.count_obj = count_obj
        self.object_manager = object_manager
        self.line_manager = line_manager
        self.movement_manager = movement_manager

        # Создание кругов и линий
        self.circles = [self.object_manager.create_random_object() for _ in range(self.count_obj)]
        for circle in self.circles:
            self.object_manager.add_object(circle)
        self.lines = self.create_lines()

    def create_lines(self):
        for i in range(len(self.circles)):
            for j in range(i + 1, len(self.circles)):
                line = self.line_manager.create_line(self.circles[i], self.circles[j])
                self.line_manager.add_line(line)
        return self.line_manager.get_lines()

    def move_figures(self):
        self.movement_manager.move(self.object_manager.get_object())
        self.line_manager.get_lines().sort()

    def repel_circle(self, pos: Vector, radius: int):
        objects = self.object_manager.get_objects_from_circle(pos, radius)
        for obj in objects:
            force_vector = obj.pos - pos
            current_vector = obj.direction
            result_vector = force_vector + current_vector

            obj.direction = result_vector * (current_vector.length / result_vector.length)
            print(f"now direction {obj.direction}")
