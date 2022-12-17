#!/usr/bin/env python3

from collections import namedtuple
from re import match
from pathlib import Path
from typing import Optional
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Point = namedtuple("Point", ["x", "y"])

	class _Area:
		def __init__(self, p1: "Solution._Point", p2: "Solution._Point"):
			self.p1 = p1
			self.p2 = p2
		
		def __repr__(self) -> str:
			return f"<Target x={{{self.p1.x}}} y={{{self.p1.y}}} w={{{self.width()}}} h={{{self.height()}}} />"
		
		def width(self) -> int:
			return self.p2.x - self.p1.x
		
		def height(self) -> int:
			return self.p2.y - self.p1.y

	def _parse_input(self, input_file_lines: list[str]) -> _Area:
		input_re_match = match(r"target area: x=([\-0-9]+)\.\.([=\-0-9]+), y=([=\-0-9]+)\.\.([=\-0-9]+)\n?", input_file_lines[0])
		assert input_re_match is not None
		p1 = Solution._Point(int(input_re_match.group(1)), int(input_re_match.group(3)))
		p2 = Solution._Point(int(input_re_match.group(2)), int(input_re_match.group(4)))
		return Solution._Area(p1, p2)


	def _plot_velocity(self, x_vel: int, y_vel: int, limit_x: int, limit_y: int) -> list[_Point]:
		cur = Solution._Point(0, 0)

		plot: list[Solution._Point] = [ cur ]

		while  cur.x < limit_x and cur.y > limit_y:
			cur = Solution._Point(cur.x + x_vel, cur.y + y_vel)
			plot.append(cur)

			x_vel += -1 if (x_vel > 0) else 1 if (x_vel < 0) else 0
			y_vel -= 1 # due to gravity

		return plot

	def _trajectory_intersects_area(self, trajectory: list[_Point], area: _Area) -> bool:
		for point in trajectory:
			if (point.x >= min(area.p1.x, area.p2.x) and point.x <= max(area.p1.x, area.p2.x) and
					point.y >= min(area.p1.y, area.p2.y) and point.y <= max(area.p1.y, area.p2.y)):
				return True
		return False

	def _get_trajectory_max_y(self, trajectory: list[_Point]) -> int:
		return max([point.y for point in trajectory])

	def part_1(self) -> int:
		best_vel_max_y: Optional[int] = None

		for x_vel in range(0, self.input.p2.x):
			for y_vel in range(150):
				trajectory = self._plot_velocity(x_vel, y_vel, self.input.p2.x + 1, self.input.p1.y - 1)
				if self._trajectory_intersects_area(trajectory, self.input):
					trajectory_max_y = self._get_trajectory_max_y(trajectory)
					if best_vel_max_y is None or trajectory_max_y > best_vel_max_y:
						best_vel_max_y = trajectory_max_y
		return best_vel_max_y


	def part_2(self) -> int:
		hit_velocities: list[Solution._Point] = []

		for x_vel in range(500):
			for y_vel in range(self.input.p1.y, 500):
				trajectory = self._plot_velocity(x_vel, y_vel, self.input.p2.x + 1, self.input.p1.y - 1)
				if self._trajectory_intersects_area(trajectory, self.input):
					hit_velocities.append(Solution._Point(x_vel, y_vel))

		return len(hit_velocities)


	def main(self) -> None:
		print(f"1. The highest y position reached is: {self.part_1()}")
		print(f"2. The number of initial velocities that hit the target is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
