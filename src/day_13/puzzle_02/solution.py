#!/usr/bin/env python3

from pathlib import Path
from src.day_13.puzzle_01.solution import Map, parse_input, fold, get_dot_points


def print_map(map: Map) -> None:
	for row in map:
		for col in row:
			print("#" if col else ".", end="")
		print()


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

	print_map(map)
	return


if __name__ == "__main__":
	main()
