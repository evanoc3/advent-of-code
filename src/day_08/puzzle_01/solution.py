#!/usr/bin/env python3

from pathlib import Path
from re import match


def parse_input(input_lines: list[str]) -> list[str]:
	return[ line.split("|")[1].strip().split(" ") for line in input_lines ]


def count_occurrences(flat_output_segments: list[list[str]]) -> dict[int, int]:
	return {
		1: len([ seg for seg in flat_output_segments if len(seg) == 2 ]),
		4: len([ seg for seg in flat_output_segments if len(seg) == 4 ]),
		7: len([ seg for seg in flat_output_segments if len(seg) == 3 ]),
		8: len([ seg for seg in flat_output_segments if len(seg) == 7 ])
	}


def main() -> None:
	output_segments: list[list[str]] = []

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		output_segments = parse_input(input_file.readlines())

	flat_output_segments = [item for sublist in output_segments for item in sublist]
	occurrences = count_occurrences(flat_output_segments)

	print(f"The total number of occurrences of 1,4,7,8 in the output is: {sum(occurrences.values())}")
	return


if __name__ == "__main__":
	main()
