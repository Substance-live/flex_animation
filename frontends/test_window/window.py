import pygame

from animation.action.engine import Engine, EngineConfig


class Game:
    """Класс-шаблон для игр на базе test_window.

    Для старта необходимо вызвать метод run().

    АТРИБУТЫ:
    ---------
    BLACK, WHITE, RED,
    GREEN, BLUE : tuple         -- цвета в RGB.
    WIDTH, HEIGHT : int     -- ширина и высота окна.
                                   Для них определены геттеры @property.
    __FPS : int                 -- количество кадров в секунду.

    МЕТОДЫ:
    -------
    init(ШИРИНА: int,
             ВЫСОТА: int,
             ЗАГОЛОВОК: str,
             КАДРЫ_В_СЕКУНДУ: int) -- конструктор класса.
    __draw()                       -- формирует изображение.
    __act()                        -- сюда вставить необходимые расчёты.
    run()                          -- запуск test_window.

    ПРИМЕЧАНИЕ:
    -----------
    Образец для запуска кода:
    game = Game(1024, 768, "Шаблон test_window", 60)
    game.run()
    """
    # Задаём цвета
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, screen_size: tuple[int, int], caption: str, fps: int, config: EngineConfig, circle_color=BLUE, line_color=BLUE):
        """Конструктор, настройка основных параметров."""
        # Инициализация test_window и настройки окна
        pygame.init()

        # Настройка ширины и высоты окна
        self.__size = screen_size
        self.__WIDTH = self.__size[0]
        self.__HEIGHT = self.__size[1]

        # Установка заголовка окна
        pygame.display.set_caption(caption)

        # Инициализация сцены и установка размера
        self.scene = pygame.display.set_mode(self.__size)

        # Инициализация логики
        self.engine = Engine(self.__size, config)

        # Инициализация кастомных цветов
        self.circle_color = circle_color
        self.line_color = line_color

        # Убрать комментарий, если нужно развёрнутое на весь экран окно
        # self.scene = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        # Для работы с задержкой и организации FPS
        self.clock = pygame.time.Clock()
        self.__FPS = fps

        # Маркер "идёт ли игра"
        self.playGame = True

    @property
    def WIDTH(self):
        return self.__WIDTH

    @property
    def HEIGHT(self):
        return self.__HEIGHT

    def __draw(self):
        """Формирует изображение.
        Вызывать метод следует между очисткой и обновлением экрана."""

        for line in self.engine.lines:
            if line.brightness is None:
                continue

            color = tuple((self.circle_color[i] * line.brightness for i in range(3)))
            pygame.draw.line(self.scene, color, line.start_pos, line.end_pos, line.width)

        for circle in self.engine.circles:
            pygame.draw.circle(self.scene, self.BLUE, circle.pos, circle.radius, 0)

    def __act(self):
        """Метод для расчётов. Вызывать после обновления экрана."""
        self.engine.move_figures()

    def run(self):
        """Главный цикл игры."""
        while self.playGame:
            # Проверяем нажатые клавиши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playGame = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playGame = False

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                continue

            # Очищаем сцену
            self.scene.fill(self.BLACK)

            # Формируем изображение
            self.__draw()

            # Отрисовываем изображения
            pygame.display.flip()

            # Расчёты
            self.__act()

            # Задержка для синхронизации FPS
            self.clock.tick(self.__FPS)

        # Выход
        pygame.quit()

