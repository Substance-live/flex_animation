# windows.py
import pygame

from application.engine.engine import Engine
from application.managers.manager import GameObjectManager, LineManager, MovementManager

from infrastructure.factories.factory import CircleFactory, DefaultLineFactory
from infrastructure.lines.line import DefaultBrightnessCalculator, BrightnessComparisonStrategy

from core.models.config import DataConfig

class Game:
    """Класс-шаблон для игр на базе test_window."""
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, screen_size: tuple[int, int], caption: str, fps: int, config: DataConfig, circle_color=BLUE, line_color=BLUE):
        pygame.init()
        self.__size = screen_size
        self.__WIDTH = self.__size[0]
        self.__HEIGHT = self.__size[1]
        pygame.display.set_caption(caption)
        self.scene = pygame.display.set_mode(self.__size)

        obj_manager = GameObjectManager(self.__size, config.circle_radius, config.start_speed, CircleFactory())
        line_manager = LineManager(config.upper_limit, config.lower_limit, config.width_of_line,
                                   DefaultLineFactory(DefaultBrightnessCalculator(), BrightnessComparisonStrategy()))
        movement_manager = MovementManager(self.__size)

        self.engine = Engine(self.__size, config.count_obj, obj_manager, line_manager, movement_manager)

        self.circle_color = circle_color
        self.line_color = line_color

        self.clock = pygame.time.Clock()
        self.__FPS = fps

        self.playGame = True

    @property
    def WIDTH(self):
        return self.__WIDTH

    @property
    def HEIGHT(self):
        return self.__HEIGHT

    def __draw(self):
        """Отрисовывает линии и круги."""
        for line in self.engine.lines:
            if line.brightness is None:
                continue
            color = tuple((self.circle_color[i] * line.brightness for i in range(3)))
            pygame.draw.line(self.scene, color, line.get_start_pos(), line.get_end_pos(), line.width)

        for obj in self.engine.circles:
            pygame.draw.circle(self.scene, self.BLUE, obj.pos, obj.radius)

            # pygame.draw.rect(self.scene, self.BLUE,
            #                  (*obj.pos, obj.side, obj.side))

    def __act(self):
        """Обновление состояния объектов."""
        self.engine.move_figures()

    def run(self):
        """Главный цикл игры."""
        while self.playGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playGame = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playGame = False

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                continue

            self.scene.fill(self.BLACK)
            self.__draw()
            pygame.display.flip()
            self.__act()
            self.clock.tick(self.__FPS)

        pygame.quit()
