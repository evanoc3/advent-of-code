#!/usr/bin/env python3

from pathlib import Path


def main() -> None:
	input_file_path = Path(__file__).parent / "input.txt"

	with open(input_file_path, "r") as input_file:
		depth, prev_depth = None, None
		increase_counter = 0

		line = input_file.readline() 
		while line:
			prev_depth = depth
			depth = int(line)
			if prev_depth is not None and depth > prev_depth:
				# print(f"Current depth ({depth}) is greater than previous ({prev_depth})")
				increase_counter += 1
			line = input_file.readline()
		
		print(f"There were {increase_counter} occurrences where the depth increased")


if __name__ == "__main__":
	main()