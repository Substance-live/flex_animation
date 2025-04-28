from dataclasses import dataclass

@dataclass
class DataConfig:
    count_obj: int
    circle_radius: int
    start_speed: float
    width_of_line: int
    upper_limit: int
    lower_limit: int
    radius_of_LCM: int
