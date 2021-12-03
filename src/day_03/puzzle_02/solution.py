#!/usr/bin/env python3

from pathlib import Path
from src.day_03.puzzle_01.solution import 


def get_oxygen_generator_rating(diagnostic_report: list[str]) -> int:
	column = 0
	while len(diagnostic_report) > 1:
		ones, zeros = 0, 0

		for line in diagnostic_report:
			bit = line[column]
			if bit == 1:
				ones += 1
			else: # bit == 0
				zeros += 1
		
		if ones >= zeros:
			diagnostic_report = [line for line in diagnostic_report if line[column] == "1"]
		else:
			diagnostic_report = [line for line in diagnostic_report if line[column] == "0"]
		
		column += 1
	return 0


def main() -> None:
	diagnostic_report: list[str] = []

	# Read the input file
	input_file_path = Path(__file__).parent / "input.txt"
	with open(input_file_path, "r") as input_file:
		diagnostic_report = input_file.readlines()


if __name__ == "__main__":
	main()
