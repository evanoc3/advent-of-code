#!/usr/bin/env python3

from pathlib import Path
from src.day_11.puzzle_01.solution import Octopus, Map, parse_input, get_adjacent_points, find_high_energy_levels


def did_all_octopii_flash(map: Map) -> bool:
	for row in map:
		for octopus in row:
			if not octopus.has_flashed:
				return False
	return True


def simulate_tick(map: Map) -> bool:
	# increase each octopuses energy level by 1
	for row in map:
		for octopus in row:
			octopus.energy_level += 1
	
	# now check if any octopus has gained enough energy to flash
	high_energy_level_points = find_high_energy_levels(map)
	while len(high_energy_level_points) > 0:
		for high_energy_point in high_energy_level_points:
			high_energy_octopus = map[high_energy_point[1]][high_energy_point[0]]
			high_energy_octopus.has_flashed = True

			adjacent_points = get_adjacent_points(map, high_energy_point)
			for adjacent_point in adjacent_points:
				adjacent_octopus = map[adjacent_point[1]][adjacent_point[0]]
				adjacent_octopus.energy_level += 1

		high_energy_level_points = find_high_energy_levels(map)
	
	if did_all_octopii_flash(map):
		return True
	
	# reset flashed octopi
	for row in map:
		for octopus in row:
			if octopus.has_flashed:
				octopus.energy_level = 0
				octopus.has_flashed = False

	return False


def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"
	map: Map
	with open(input_file_path, "r") as input_file:
		map = parse_input(input_file.readlines())
	
	day = 0
	all_octopii_did_flash = False
	while not all_octopii_did_flash:
		all_octopii_did_flash = simulate_tick(map)
		day += 1

	print(f"On day {day}, all octopii flashed together")
	return


if __name__ == "__main__":
	main()
