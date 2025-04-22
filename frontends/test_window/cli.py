
from core.models.config import DataConfig

from .window import Game
from .args import parse_args
from .config_reader import read_config

def main() -> None:
    config = DataConfig(*parse_args())
    screen_size, fps = read_config()

    game = Game(screen_size, "Test window", fps, config)
    game.run()
