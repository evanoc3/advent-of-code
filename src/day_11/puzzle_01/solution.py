#!/usr/bin/env python3

from pathlib import Path
from typing import Optional
from src.day_09.puzzle_01.solution import Point


class Octopus:
	def __init__(self, energy_level: int):
		self.energy_level = energy_level
		self.has_flashed = False


Map = list[list[Octopus]]


def parse_input(input_lines: list[str]) -> list[list[Octopus]]:
	map: list[list[Octopus]] = []
	for row in input_lines:
		map.append([ Octopus(int(col)) for col in row.strip() ])
	return map


def find_high_energy_levels(map: Map) -> Optional[Point]:
	points: list[Point] = []
	for y in range(len(map)):
		row = map[y]
		for x in range(len(row)):
			octopus: Octopus = map[y][x]
			if octopus.energy_level > 9 and not octopus.has_flashed:
				points.append((x, y))
	return points


def get_adjacent_points(height_map: Map, point: Point) -> list[Point]:
	min_y, min_x = 0, 0
	max_y, max_x = len(height_map) - 1, len(height_map[0]) - 1

	x, y = point[0], point[1]

	has_top, has_bottom = y > min_y, y < max_y
	has_left, has_right = x > min_x, x < max_x

	adjacent_points: list[int] = []
	if has_top:
		adjacent_points.append((x, y-1)) # top adjacent point
	if has_bottom:
		adjacent_points.append((x, y+1)) # bottom adjacent point
	if has_left:
		adjacent_points.append((x-1, y)) # left adjacent point
	if has_right:
		adjacent_points.append((x+1, y)) # right adjacent point
	if has_top and has_left:
		adjacent_points.append((x-1, y-1)) # top-left adjacent point
	if has_top and has_right:
		adjacent_points.append((x+1, y-1)) # top-right adjacent point
	if has_bottom and has_left:
		adjacent_points.append((x-1, y+1)) # bottom-left adjacent point
	if has_bottom and has_right:
		adjacent_points.append((x+1, y+1)) # bottom-right adjacent point
	
	return adjacent_points


def simulate_tick(map: Map) -> tuple[Map, int]:
	new_flashes = 0

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
			new_flashes += 1

			adjacent_points = get_adjacent_points(map, high_energy_point)
			for adjacent_point in adjacent_points:
				adjacent_octopus = map[adjacent_point[1]][adjacent_point[0]]
				adjacent_octopus.energy_level += 1

		high_energy_level_points = find_high_energy_levels(map)
	
	# reset flashed octopi
	for row in map:
		for octopus in row:
			if octopus.has_flashed:
				octopus.energy_level = 0
				octopus.has_flashed = False

	return map, new_flashes


def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"
	map: Map
	with open(input_file_path, "r") as input_file:
		map = parse_input(input_file.readlines())
	
	day, flashes = 0, 0
	while day < 100:
		map, new_flashes = simulate_tick(map)
		flashes += new_flashes
		day += 1

	print(f"By day {day}, there had been a total of {flashes} flashes")
	return


if __name__ == "__main__":
	main()
