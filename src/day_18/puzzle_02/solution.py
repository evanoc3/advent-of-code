#!/usr/bin/env python3

from pathlib import Path
from typing import Optional
from src.day_18.puzzle_01.solution import SnailFishNumber, parse_input, add_numbers, get_magnitude


def main() -> None:
	nums: list[SnailFishNumber] = []

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		nums = parse_input(input_file.readlines())
	
	highest_nums_indexes: Optional[tuple[int, int]] = None
	highest_magnitude: Optional[int] = None
	
	for i in range(len(nums)):
		for j in range(len(nums)):
			if i == j:
				continue
			
			sum = add_numbers(nums[i], nums[j])
			magnitude = get_magnitude(sum)

			if highest_magnitude is None or magnitude > highest_magnitude:
				highest_magnitude = magnitude
				highest_nums_indexes = (i, j)
	
	print(f"The highest magnitude found by adding two numbers is: {highest_magnitude}")
	return


if __name__ == "__main__":
	main()
