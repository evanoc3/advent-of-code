#!/usr/bin/env python3

from pathlib import Path
from src.day_17.puzzle_01.solution import Point, Area, parse_input, plot_velocity, trajectory_intersects_area


def main() -> None:
	target: Area

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		target = parse_input(input_file.readline())
	
	hit_velocities: list[Point] = []

	for x_vel in range(500):
		for y_vel in range(target.p1.y, 500):
			trajectory = plot_velocity(x_vel, y_vel, target.p2.x + 1, target.p1.y - 1)
			if trajectory_intersects_area(trajectory, target):
				hit_velocities.append(Point(x_vel, y_vel))

	print(f"The number of initial velocities that hit the target is: {len(hit_velocities)}")
	return


if __name__ == "__main__":
	main()
