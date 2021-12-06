#!/usr/bin/env python3

from pathlib import Path


def parse_input(input_line: str) -> dict[int, int]:
	fishes = [int(x) for x in input_line.split(",")]
	return {
		0: len([fish for fish in fishes if fish == 0]),
		1: len([fish for fish in fishes if fish == 1]),
		2: len([fish for fish in fishes if fish == 2]),
		3: len([fish for fish in fishes if fish == 3]),
		4: len([fish for fish in fishes if fish == 4]),
		5: len([fish for fish in fishes if fish == 5]),
		6: len([fish for fish in fishes if fish == 6]),
		7: len([fish for fish in fishes if fish == 7]),
		8: len([fish for fish in fishes if fish == 8])
	}



def simulation_tick(fishes: dict[int, int]) -> dict[int, int]:
	new_fishes = fishes[0]

	for i in range(0, 8):
		fishes[i] = fishes[i+1]
	fishes[8] = new_fishes
	fishes[6] += new_fishes

	return fishes


def total_fishes(fishes: dict[int, int]) -> int:
	accumulator = 0
	for x in fishes.values():
		accumulator += x
	return accumulator


def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"

	fishes: dict[int, int] = {
		0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0
	}

	with open(input_file_path, "r") as input_file:
		fishes = parse_input(input_file.readline())
	
	for i in range(1, 257):
		fishes = simulation_tick(fishes)
		if i == 256:
			print(f"Day {i}. fish population: {total_fishes(fishes)}")
	return


if __name__ == "__main__":
	main()
