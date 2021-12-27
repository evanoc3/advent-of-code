#!/usr/bin/env python3

from itertools import product
from pathlib import Path
from src.day_19.puzzle_01.solution import parse_input, get_beacons


def main() -> None:
	detected_beacons: list[list[tuple[int, int, int]]]

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		detected_beacons = parse_input(input_file.readlines())
	
	_, shifts = get_beacons(detected_beacons)
	sxs = product(shifts,shifts)
	print(max(sum(abs(a-b) for a, b in zip(l, r)) for l, r in sxs))
	return


if __name__ == "__main__":
	main()
