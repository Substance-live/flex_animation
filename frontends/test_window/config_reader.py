from pathlib import Path

def read_config() -> tuple[tuple[int, int], int]:
    config_path = Path(__file__).parent / "config.txt"
    with config_path.open() as f:
        content = f.read().replace('\n', '=').split('=')

        return (int(content[1]), int(content[3])), int(content[5])
