#!/usr/bin/env python3

from copy import deepcopy
from pathlib import Path
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	class _Lanternfish:
		def __init__(self, age: int = 8):
			self.reproduction_timer = age

	def _parse_input(self, input_files_lines: list[str]) -> list[_Lanternfish]:
		return [ Solution._Lanternfish(int(age)) for age in input_files_lines[0].split(",") ]


	def _part_1_simulation_tick(self, fishes: list[_Lanternfish]) -> list[_Lanternfish]:
		new_fishes: list[Solution._Lanternfish] = []

		for fish in fishes:
			if fish.reproduction_timer == 0:
				new_fishes.append(Solution._Lanternfish())
				fish.reproduction_timer = 6
			else:
				fish.reproduction_timer -= 1
		
		fishes.extend(new_fishes)
		return fishes

	def part_1(self) -> int:
		fishes = deepcopy(self.input)
		for _ in range(80):
			self._part_1_simulation_tick(fishes)
		return len(fishes)


	def _create_buckets(self, fishes: list[_Lanternfish]) -> dict[int, int]:
		fish_ages = [fish.reproduction_timer for fish in fishes]
		return {
			0: len([fish for fish in fish_ages if fish == 0]),
			1: len([fish for fish in fish_ages if fish == 1]),
			2: len([fish for fish in fish_ages if fish == 2]),
			3: len([fish for fish in fish_ages if fish == 3]),
			4: len([fish for fish in fish_ages if fish == 4]),
			5: len([fish for fish in fish_ages if fish == 5]),
			6: len([fish for fish in fish_ages if fish == 6]),
			7: len([fish for fish in fish_ages if fish == 7]),
			8: len([fish for fish in fish_ages if fish == 8])
		}

	def _part_2_simulation_tick(self, fishes: dict[int, int]) -> dict[int, int]:
		new_fishes = fishes[0]

		for i in range(0, 8):
			fishes[i] = fishes[i+1]
		fishes[8] = new_fishes
		fishes[6] += new_fishes

		return fishes
	
	def _total_fishes(self, fishes: dict[int, int]) -> int:
		accumulator = 0
		for x in fishes.values():
			accumulator += x
		return accumulator

	def part_2(self) -> int:
		fish_buckets = self._create_buckets(self.input)
		for _ in range(256):
			fish_buckets = self._part_2_simulation_tick(fish_buckets)
		return self._total_fishes(fish_buckets)


	def main(self) -> None:
		print(f"Day 80. fish population: {self.part_1()}")
		print(f"Day 256. fish population: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()