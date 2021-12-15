#!/usr/bin/env python3

from copy import deepcopy
from pathlib import Path
from src.day_09.puzzle_01.solution import Map, parse_input
from src.day_15.puzzle_01.solution import get_total_risk_of_path, get_least_risky_path


def create_new_map_segment(map: Map, increment: int) -> Map:
	new_map = deepcopy(map)

	for _ in range(increment):
		for y in range(len(map)):
			for x in range(len(map[0])):
				new_map[y][x] += 1 if new_map[y][x] < 9 else 2
				new_map[y][x] %= 10
	
	return new_map


def expand_map(map: Map) -> Map:
	new_map = []
	for yi in range(5):
		row_segment = []

		for xi in range(5):
			i = yi + xi
			new_map_segment = create_new_map_segment(map, i)
			if not row_segment:
				row_segment = new_map_segment
			else: # len(row_segment) > 0
				for j in range(len(row_segment)):
					row_segment[j].extend(new_map_segment[j])

		new_map.extend(row_segment)

	return new_map


def main() -> None:
	map: Map
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		map = parse_input(input_file.readlines())
	map = expand_map(map)

	end_point = (len(map)-1, len(map[0])-1)
	path = get_least_risky_path(map, (0,0), end_point)
	print(f"The least risky path has a total risk of: {get_total_risk_of_path(map, path[1:])}")
	return


if __name__ == "__main__":
	main()
