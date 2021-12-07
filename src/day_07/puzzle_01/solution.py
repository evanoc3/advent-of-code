#!/usr/bin/env python3

from pathlib import Path


def sum_distance(crab_positions: list[int], position: int) -> int:
	return sum([abs(crab_position - position) for crab_position in crab_positions])


def parse_input(input_line: str) -> list[int]:
	return [int(x) for x in input_line.split(",")]


def main() -> None:
	crab_positions: list[int]

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		crab_positions = parse_input(input_file.readline())

	max_pos = max(crab_positions)
	sum_distances: list[int] = []

	for position in range(max_pos):
		sum_distances.append( sum_distance(crab_positions, position) )
	
	min_sum_distance = min(sum_distances)
	min_sum_distance_index = sum_distances.index(min_sum_distance)

	print(f"Lowest sum distance: {min_sum_distance} at position: {min_sum_distance_index}")
	return


if __name__ == "__main__":
	main()
