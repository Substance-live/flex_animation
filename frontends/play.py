from core.models.config import DataConfig

from test_window.window import Game

screen_size = (1948, 1052)
fps = 60
config = DataConfig(
    count_obj=2,
    circle_radius=15,
    start_speed=1.51,
    width_of_line=10,
    upper_limit=0,
    lower_limit=300,
    radius_of_LCM=100,
)

if __name__ == '__main__':
    game = Game(screen_size, "Test window", fps, config)
    game.run()
