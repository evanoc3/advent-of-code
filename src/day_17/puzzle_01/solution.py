#!/usr/bin/env python3

from re import match
from pathlib import Path
from typing import Optional


class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y
	
	def __repr__(self) -> str:
		return f"({self.x}, {self.y})"


class Area:
	def __init__(self, p1: Point, p2: Point):
		self.p1 = p1
		self.p2 = p2
	
	def __repr__(self) -> str:
		return f"<Target x={{{self.p1.x}}} y={{{self.p1.y}}} w={{{self.width()}}} h={{{self.height()}}} />"
	
	def width(self) -> int:
		return self.p2.x - self.p1.x
	
	def height(self) -> int:
		return self.p2.y - self.p1.y


def parse_input(input_line: str) -> Area:
	input_re_match = match(r"target area: x=([\-0-9]+)\.\.([=\-0-9]+), y=([=\-0-9]+)\.\.([=\-0-9]+)\n?", input_line)
	assert input_re_match is not None
	p1 = Point(int(input_re_match.group(1)), int(input_re_match.group(3)))
	p2 = Point(int(input_re_match.group(2)), int(input_re_match.group(4)))
	return Area(p1, p2)


def plot_velocity(x_vel: int, y_vel: int, limit_x: int, limit_y: int) -> list[Point]:
	cur = Point(0, 0)

	plot: list[Point] = [ cur ]

	while not (cur.x > limit_x or (x_vel == 0 and cur.y < limit_y)):
		cur = Point(cur.x + x_vel, cur.y + y_vel)
		plot.append(cur)

		x_vel += -1 if (x_vel > 0) else 1 if (x_vel < 0) else 0
		y_vel -= 1 # due to gravity

	return plot


def trajectory_intersects_area(trajectory: list[Point], area: Area) -> bool:
	for point in trajectory:
		if (point.x >= min(area.p1.x, area.p2.x) and point.x <= max(area.p1.x, area.p2.x) and
				point.y >= min(area.p1.y, area.p2.y) and point.y <= max(area.p1.y, area.p2.y)):
			return True
	return False


def get_trajectory_max_y(trajectory: list[Point]) -> int:
	return max([point.y for point in trajectory])


def main() -> None:
	target: Area

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		target = parse_input(input_file.readline())
	
	best_vel: Optional[Point] = None
	best_vel_max_y: Optional[int] = None

	for x_vel in range(0, target.p2.x):
		for y_vel in range(150):
			trajectory = plot_velocity(x_vel, y_vel, target.p2.x + 1, target.p1.y - 1)
			if trajectory_intersects_area(trajectory, target):
				trajectory_max_y = get_trajectory_max_y(trajectory)
				if best_vel_max_y is None or trajectory_max_y > best_vel_max_y:
					best_vel = Point(x_vel, y_vel)
					best_vel_max_y = trajectory_max_y

	print(f"The inital velocities which created the trajectory with the highest peak y is: {best_vel}, with peak y: {best_vel_max_y}")
	return


if __name__ == "__main__":
	main()
