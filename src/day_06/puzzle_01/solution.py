#!/usr/bin/env python3

from pathlib import Path
from typing import Optional


class Lanternfish:
	def __init__(self, age: Optional[int]):
		self.reproduction_timer = age if age else 8


def parse_input(input_line: str) -> list[Lanternfish]:
	return [ Lanternfish(int(age)) for age in input_line.split(",") ]


def simulation_tick(fishes: list[Lanternfish]) -> list[Lanternfish]:
	new_fishes: list[Lanternfish] = []

	for fish in fishes:
		if fish.reproduction_timer == 0:
			new_fishes.append(Lanternfish(8))
			fish.reproduction_timer = 6
		else:
			fish.reproduction_timer -= 1
	
	fishes.extend(new_fishes)
	return fishes



def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"

	fishes: list[Lanternfish] = []

	with open(input_file_path, "r") as input_file:
		fishes = parse_input(input_file.readline())
	
	for i in range(1, 81):
		simulation_tick(fishes)
		if i == 80:
			print(f"Day {i}. fish population: {len(fishes)}")
	
	return


if __name__ == "__main__":
	main()
