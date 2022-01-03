#!/usr/bin/env python3

from collections import namedtuple
from pathlib import Path
from re import match


Cuboid = namedtuple("Cuboid", ["min_x", "max_x", "min_y", "max_y", "min_z", "max_z", "sign"])


def main() -> None:
	cuboids: list[Cuboid] = []
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		cuboids = parse_input(input_file.readlines())
	
	grid = {}

	for cuboid in cuboids:
		if cuboid.min_x < -50 or cuboid.max_x > 50 or cuboid.min_y < -50 or cuboid.max_y > 50 or cuboid.min_z < -50 or cuboid.max_z > 50:
			continue
		
		for x in range(cuboid.min_x, cuboid.max_x + 1):
			for y in range(cuboid.min_y, cuboid.max_y + 1):
				for z in range(cuboid.min_z, cuboid.max_z + 1):
					grid[x, y, z] = 1 if cuboid.sign == 1 else 0

	print(f"There are {count_active_cells(grid)} active cells within the bounds (-50, -50, -50) - (50, 50, 50)")
	return


def parse_input(input_lines: list[str]):
	output = []
	for input_line in input_lines:
		re_match = match(r"(on|off) x=([+\-0-9]+)\.\.([+\-0-9]+),y=([+\-0-9]+)\.\.([+\-0-9]+),z=([+\-0-9]+)\.\.([+\-0-9]+)\n?", input_line)
		if re_match:
			min_x, max_x = min(int(re_match.group(2)), int(re_match.group(3))), max(int(re_match.group(2)), int(re_match.group(3)))
			min_y, max_y = min(int(re_match.group(4)), int(re_match.group(5))), max(int(re_match.group(4)), int(re_match.group(5)))
			min_z, max_z = min(int(re_match.group(6)), int(re_match.group(7))), max(int(re_match.group(6)), int(re_match.group(7)))
			sign = 1 if re_match.group(1) == "on" else -1
			output.append(Cuboid(min_x, max_x, min_y, max_y, min_z, max_z, sign))
	return output


def count_active_cells(grid: dict) -> int:
	return sum(grid.values())


if __name__ == "__main__":
	main()
