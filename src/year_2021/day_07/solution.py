#!/usr/bin/env python3

from pathlib import Path
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _parse_input(self, input_file_lines: list[str]) -> list[int]:
		return [int(x) for x in input_file_lines[0].split(",")]


	def _part_1_sum_distances(self, crab_positions: list[int], position: int) -> int:
		return sum([abs(crab_position - position) for crab_position in crab_positions])

	def part_1(self) -> int:
		max_pos = max(self.input)
		sum_distances: list[int] = [ self._part_1_sum_distances(self.input, i) for i in range(max_pos) ] 

		return min(sum_distances)


	def _part_2_sum_distances(self, crab_positions: list[int], position: int) -> int:
		distances = [ abs(position - crab_position) for crab_position in crab_positions ]
		return sum([ int((distance ** 2 + distance) / 2) for distance in distances ])

	def part_2(self) -> None:
		max_pos = max(self.input)
		sum_distances: list[int] = [ self._part_2_sum_distances(self.input, i) for i in range(max_pos) ]
		return min(sum_distances)


	def main(self) -> None:
		print(f"1. Lowest sum distance: {self.part_1()}")
		print(f"2. Lowest sum distance: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
