from animation.action.engine import EngineConfig

from test_window.window import Game

screen_size = (1024, 768)
fps = 60
config = EngineConfig(
    count_obj = 25,
    circle_radius = 15,
    start_speed= 1.25,
    width_of_line = 10,
    upper_limit = 50,
    lower_limit = 250
)

if __name__ == '__main__':
    game = Game(screen_size, "Test window", fps, config)
    game.run()
