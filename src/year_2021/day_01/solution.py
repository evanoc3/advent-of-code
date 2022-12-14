#!/usr/bin/env python3

from pathlib import Path
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _parse_input(self, input_file_lines: list[str]) -> list[int]:
		return [int(line) for line in input_file_lines]
	

	def part_1(self) -> int:
		depth, prev_depth = None, None
		increase_counter = 0

		for measurement in self.input:
			prev_depth = depth
			depth = measurement
			if prev_depth is not None and depth > prev_depth:
				increase_counter += 1
		
		return increase_counter
	

	class _SlidingWindow:
		def __init__(self, measurements: list[int], lines: list[int]) -> None:
			self.measurements = measurements
			self.lines = lines
		
		def sum(self) -> int:
			return sum(self.measurements)
		
		def __str__(self) -> str:
			return f"<SlidingWindow sum={self.sum()} measurements=[{', '.join([str(x) for x in self.measurements])}] lines=[{', '.join([str(x) for x in self.lines])}] />"

	def part_2(self) -> int:
		increase_counter = 0
		window, prev_window = None, None

		for i in range(1, len(self.input) - 1):
			prev_window = window
			window = Solution._SlidingWindow(measurements=self.input[i-1:i+2], lines=[i-1, i, i+1])

			if prev_window is not None and window.sum() > prev_window.sum():
				increase_counter += 1

		return increase_counter


	def main(self) -> None:
		print(f"1. There were {self.part_1()} occurrences where the depth increased")
		print(f"2. There were {self.part_2()} increases in 3-point sliding window averages")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
