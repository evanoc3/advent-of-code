#!/usr/bin/env python3

from pathlib import Path
from re import match
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Command = tuple[str, int]

	def _parse_input(self, input_file_lines: list[str]) -> list[_Command]:
		output = []
		for input_line in input_file_lines:
			result = match(r"^(forward|up|down)\s(\d+)$", input_line)
			output.append((result.group(1).lower(), int(result.group(2))))
		return output
	
	
	def _part_1_get_coordinates(self, commands: list[_Command]) -> tuple[int, int]:
		x, y = 0, 0
		
		for command, magnitude in commands:
			if command == "forward":
				x += magnitude
			elif command == "up":
				y -= magnitude
			elif command == "down":
				y += magnitude
		return x, y

	def part_1(self) -> int:
		x, y = self._part_1_get_coordinates(self.input)
		return x * y


	def _part_2_get_coordinates(self, commands: list[_Command]) -> tuple[int, int]:
		x, y, aim = 0, 0, 0
		for command, magnitude in commands:
			if command == "forward":
				x += magnitude
				y += (aim * magnitude)
			elif command == "up":
				aim -= magnitude
			elif command == "down":
				aim += magnitude
		return x, y

	def part_2(self) -> int:
		x, y = self._part_2_get_coordinates(self.input)
		return x * y


	def main(self) -> None:
		x, y = self._part_1_get_coordinates(self.input)
		print(f"1. The resulting vector is: (x, y) = ({x}, {y}), x * y = {self.part_1()}")

		x, y = self._part_2_get_coordinates(self.input)
		print(f"1. The resulting vector is: (x, y) = ({x}, {y}), x * y = {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
