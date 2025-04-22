import argparse
from typing import NamedTuple

class Args(NamedTuple):
    count_obj: int
    circle_radius: int
    start_speed: float
    width_of_line: int
    upper_limit: int
    lower_limit: int

def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        dest="count_obj",
        type=int,
        default=25,
        help="Количество объектов (2-100)"
    )
    parser.add_argument(
        "-r",
        dest="obj_radius",
        type=int,
        default=15,
        help="Радиус круга (5-25)"
    )
    parser.add_argument(
        "-s",
        dest="start_speed",
        type=float,
        default=1.25,
        help="Начальная скорость"
    )
    parser.add_argument(
        "-w",
        dest="width_of_line",
        type=int,
        default=10,
        help="Толщина линии (5-25)"
    )
    parser.add_argument(
        "-up",
        dest="upper_limit",
        type=int,
        default=50,
        help="Вверхняя граница"
    )
    parser.add_argument(
        "-low",
        dest="lower_limit",
        type=int,
        default=250,
        help="Нижняя граница"
    )

    args = parser.parse_args()

    return Args(
        count_obj=args.count_obj,
        circle_radius=args.circle_radius,
        start_speed=args.start_speed,
        width_of_line=args.width_of_line,
        upper_limit=args.upper_limit,
        lower_limit=args.lower_limit
    )

