#!/usr/bin/env python3

from collections import namedtuple
from pathlib import Path
from re import match
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):
	
	_Cuboid = namedtuple("Cuboid", ["mode", "x1", "x2", "y1", "y2", "z1", "z2"])

	def _parse_input(self, input_file_lines: list[str]) -> list[_Cuboid]:
		output: list[Solution._Cuboid] = []
		for input_line in input_file_lines:
			re_match = match(r"(on|off) x=([+\-0-9]+)\.\.([+\-0-9]+),y=([+\-0-9]+)\.\.([+\-0-9]+),z=([+\-0-9]+)\.\.([+\-0-9]+)\n?", input_line)
			if re_match:
				output.append(Solution._Cuboid(
					re_match.group(1),
					int(re_match.group(2)),
					int(re_match.group(3)),
					int(re_match.group(4)),
					int(re_match.group(5)),
					int(re_match.group(6)),
					int(re_match.group(7))
				))
		return output


	def _part_1_count_active_cells(self, grid: dict) -> int:
		return sum(grid.values())

	def part_1(self) -> int:
		grid = {}

		for cub in self.input:
			min_x = min(cub.x1, cub.x2)
			max_x = max(cub.x1, cub.x2)
			min_y = min(cub.y1, cub.y2)
			max_y = max(cub.y1, cub.y2)
			min_z = min(cub.z1, cub.z2)
			max_z = max(cub.z1, cub.z2)

			if any([min_x < -50, max_x > 50, min_y < -50, max_y > 50, min_x < -50, max_y > 50]):
				continue

			for x in range(min_x, max_x + 1):
				for y in range(min_y, max_y + 1):
					for z in range(min_z, max_z + 1):
						grid[x, y, z] = 1 if cub.mode == "on" else 0

		return self._part_1_count_active_cells(grid)
	

	def _part_2_count_active_cells(self, instructions: list[_Cuboid]) -> int:
		counter = 0
		counted_zones = []

		for d in reversed(instructions):
			mode, box = d[0], d[1:]
			x1, x2, y1, y2, z1, z2 = box
			if mode == "on":
				dead_cubes = []
				for overlap_box in [ self._overlapping(zone, box) for zone in counted_zones ]:
					if overlap_box is not None:
						dead_cubes.append(("on", *overlap_box))

				counter += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
				counter -= self._part_2_count_active_cells(dead_cubes)
			counted_zones.append(box)
		return counter

	def _overlapping(self, c1: _Cuboid, c2: _Cuboid) -> _Cuboid:
		max_x, max_y, max_z = [max(c1[i], c2[i]) for i in (0, 2, 4)]
		min_x, min_y, min_z = [min(c1[i], c2[i]) for i in (1, 3, 5)]
		if min_x - max_x >= 0 and min_y - max_y >= 0 and min_z - max_z >= 0:
			return (max_x, min_x, max_y, min_y, max_z, min_z)
		return None

	def part_2(self) -> int:
		return self._part_2_count_active_cells(self.input)
	

	def main(self) -> None:
		print(f"1. There are {self.part_1()} active cells within the bounds (-50, -50, -50) - (50, 50, 50)")
		print(f"2. There are {self.part_2()} active cells in total")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
