#!/usr/bin/env python3

from re import match
from pathlib import Path
from typing import TypedDict


Map = list[list[bool]]


def parse_input(input_lines: str) -> tuple[Map, list[tuple[str, int]]]:
	dot_points: list[tuple[int, int]] = []
	fold_commands: list[tuple[str, int]] = []

	for line in input_lines:
		dot_point_re_match = match(r"(\d+),(\d+)\n?", line)
		if dot_point_re_match:
			dot_points.append((int(dot_point_re_match.group(1)), int(dot_point_re_match.group(2))))
			continue

		fold_command_re_match = match(r"fold along ([xy])=(\d+)\n?", line)
		if fold_command_re_match:
			fold_commands.append((fold_command_re_match.group(1), int(fold_command_re_match.group(2))))

	
	max_x = max([ point[0] for point in dot_points ]) + 1
	max_y = max([ point[1] for point in dot_points ]) + 1

	map: Map = []
	for y in range(max_y):
		map.append([ False for x in range(max_x) ])

	for dot_point in dot_points:
		x,y = dot_point
		map[y][x] = True

	return (map, fold_commands)


def fold(map: Map, line: int) -> Map:
	map_above_fold = map[:line]

	folded_map = map[line:][::-1]
	folded_dot_points = get_dot_points(folded_map)

	for folded_dot_point in folded_dot_points:
		x, y = folded_dot_point
		map_above_fold[y][x] = True

	return map_above_fold


def get_dot_points(map: Map) -> list[tuple[int, int]]:
	points = []
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x]:
				points.append((x, y))

	return points


def main() -> None:
	map: Map
	fold_commands: list[tuple[str, int]]

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		map, fold_commands = parse_input(input_file.readlines())
	
	for fold_command in fold_commands:
		axis, line = fold_command
		if axis == "y":
			map = fold(map, line)
		else: # axis == "x"
			inverted_map = [list(x) for x in zip(*map)]
			inverted_folded_map = fold(inverted_map, line)
			map = [list(x) for x in zip(*inverted_folded_map)]
		break

	print(f"Total dots: {len(get_dot_points(map))}")
	return


if __name__ == "__main__":
	main()
