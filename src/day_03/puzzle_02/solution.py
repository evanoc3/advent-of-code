#!/usr/bin/env python3

from pathlib import Path
from src.day_03.puzzle_01.solution import parse_binary_bits_to_int


def get_oxygen_generator_rating(diagnostic_report: list[str]) -> int:
	column = 0
	while len(diagnostic_report) > 1:
		ones, zeros = 0, 0

		for line in diagnostic_report:
			bit = line[column]
			if bit == "1":
				ones += 1
			else: # bit == 0
				zeros += 1
		
		if ones >= zeros:
			diagnostic_report = [line for line in diagnostic_report if line[column] == "1"]
		else: # ones < zeros
			diagnostic_report = [line for line in diagnostic_report if line[column] == "0"]
		
		column += 1
	
	oxygen_generator_rating_bits = [int(c) for c in diagnostic_report[0] if c in ["1", "0"]]
	return parse_binary_bits_to_int(oxygen_generator_rating_bits)


def get_C02_scrubber_rating(diagnostic_report: list[str]) -> int:
	column = 0
	while len(diagnostic_report) > 1:
		ones, zeros = 0, 0

		for line in diagnostic_report:
			bit = line[column]
			if bit == "1":
				ones += 1
			else: # bit == 0
				zeros += 1
		
		if zeros <= ones:
			diagnostic_report = [line for line in diagnostic_report if line[column] == "0"]
		else: # zeros > ones
			diagnostic_report = [line for line in diagnostic_report if line[column] == "1"]
		
		column += 1
	
	oxygen_generator_rating_bits = [int(c) for c in diagnostic_report[0] if c in ["1", "0"]]
	return parse_binary_bits_to_int(oxygen_generator_rating_bits)


def main() -> None:
	diagnostic_report: list[str] = []

	# Read the input file
	input_file_path = Path(__file__).parent / "input.txt"
	with open(input_file_path, "r") as input_file:
		diagnostic_report = input_file.readlines()
	
	oxygen_generator_rating = get_oxygen_generator_rating(diagnostic_report)
	c02_scrubber_rating = get_C02_scrubber_rating(diagnostic_report)

	print(f"Life support rating: (O2 x CO2) = ({oxygen_generator_rating} x {c02_scrubber_rating}) = {oxygen_generator_rating * c02_scrubber_rating}")
	return


if __name__ == "__main__":
	main()
