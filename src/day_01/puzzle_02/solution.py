#!/usr/bin/env python3

from pathlib import Path


class SlidingWindow:
	def __init__(self, measurements: list[int], lines: list[int]) -> None:
		self.measurements = measurements
		self.lines = lines
	
	def sum(self) -> int:
		return sum(self.measurements)
	
	def __str__(self) -> str:
		return f"<SlidingWindow sum={self.sum()} measurements=[{', '.join([str(x) for x in self.measurements])}] lines=[{', '.join([str(x) for x in self.lines])}] />"
		


def main() -> None:
	input_file_path = Path(__file__).parent / "input.txt"

	lines: list[str]
	with open(input_file_path, "r") as input_file:
		lines = input_file.readlines()

	increase_counter = 0
	window, prev_window = None, None
	for i in range(1, len(lines) - 1):
		prev_window = window
		window = SlidingWindow(measurements=[int(lines[i-1]), int(lines[i]), int(lines[i+1])], lines=[i-1, i, i+1])

		if prev_window is not None and window.sum() > prev_window.sum():
			# print(f"{window} is greater than {prev_window}")
			increase_counter += 1

	print(f"There were {increase_counter} increases in 3-point sliding window averages")
	return


if __name__ == "__main__":
	main()