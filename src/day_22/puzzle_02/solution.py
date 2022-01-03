#!/usr/bin/env python3

from pathlib import Path
from re import match


def main() -> None:
	instruction_cuboids: list

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		instruction_cuboids = parse_input(input_file.readlines())

	counter = count_active_cells(instruction_cuboids)
	print(f"2. There are {counter} active cells in total")
	return


def parse_input(input_lines: list[str]) -> list:
	output = []
	for input_line in input_lines:
		re_match = match(r"(on|off) x=([+\-0-9]+)\.\.([+\-0-9]+),y=([+\-0-9]+)\.\.([+\-0-9]+),z=([+\-0-9]+)\.\.([+\-0-9]+)\n?", input_line)
		if re_match:
			output.append((re_match.group(1), *map(int, re_match.groups()[1:])))
	return output


def count_active_cells(instructions: list) -> int:
	counter = 0
	counted_zones = []

	for d in reversed(instructions):
		mode, box = d[0], d[1:]
		x1, x2, y1, y2, z1, z2 = box
		if mode == "on":
			dead_cubes = []
			for overlap_box in [ overlapping(zone, box) for zone in counted_zones ]:
				if overlap_box is not None:
					dead_cubes.append(("on", *overlap_box))

			counter += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
			counter -= count_active_cells(dead_cubes)
		counted_zones.append(box)
	return counter


def overlapping(c1, c2):
	max_x, max_y, max_z = [max(c1[i], c2[i]) for i in (0, 2, 4)]
	min_x, min_y, min_z = [min(c1[i], c2[i]) for i in (1, 3, 5)]
	if min_x - max_x >= 0 and min_y - max_y >= 0 and min_z - max_z >= 0:
		return (max_x, min_x, max_y, min_y, max_z, min_z)
	return None


if __name__ == "__main__":
	main()
