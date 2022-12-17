#!/usr/bin/env python3

from collections import namedtuple
from copy import deepcopy
from pathlib import Path
from typing import Optional
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	class _Octopus:
		def __init__(self, energy_level: int):
			self.energy_level = energy_level
			self.has_flashed = False

	_Map = list[list[_Octopus]]

	def _parse_input(self, input_file_lines: list[str]) -> _Map:
		map: list[list[Solution._Octopus]] = []
		for row in input_file_lines:
			map.append([ Solution._Octopus(int(col)) for col in row.strip() ])
		return map


	_Point = namedtuple("Point", ["x", "y"])

	def _find_high_energy_levels(self, map: _Map) -> "Optional[Solution._Point]":
		points: list[Solution._Point] = []
		for y in range(len(map)):
			row = map[y]
			for x in range(len(row)):
				octopus: Solution._Octopus = map[y][x]
				if octopus.energy_level > 9 and not octopus.has_flashed:
					points.append((x, y))
		return points

	def _get_adjacent_points(self, height_map: _Map, point: _Point) -> list[_Point]:
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

	def _part_1_simulate_tick(self, map: _Map) -> tuple[_Map, int]:
		new_flashes = 0

		# increase each octopuses energy level by 1
		for row in map:
			for octopus in row:
				octopus.energy_level += 1
		
		# now check if any octopus has gained enough energy to flash
		high_energy_level_points = self._find_high_energy_levels(map)
		while len(high_energy_level_points) > 0:
			for high_energy_point in high_energy_level_points:
				high_energy_octopus = map[high_energy_point[1]][high_energy_point[0]]
				high_energy_octopus.has_flashed = True
				new_flashes += 1

				adjacent_points = self._get_adjacent_points(map, high_energy_point)
				for adjacent_point in adjacent_points:
					adjacent_octopus = map[adjacent_point[1]][adjacent_point[0]]
					adjacent_octopus.energy_level += 1

			high_energy_level_points = self._find_high_energy_levels(map)
		
		# reset flashed octopi
		for row in map:
			for octopus in row:
				if octopus.has_flashed:
					octopus.energy_level = 0
					octopus.has_flashed = False

		return map, new_flashes

	def part_1(self) -> int:
		map = deepcopy(self.input)
		day, flashes = 0, 0
		while day < 100:
			map, new_flashes = self._part_1_simulate_tick(map)
			flashes += new_flashes
			day += 1
		return flashes
	

	def _did_all_octopii_flash(self, map: _Map) -> bool:
		for row in map:
			for octopus in row:
				if not octopus.has_flashed:
					return False
		return True

	def _part_2_simulate_tick(self, map: _Map) -> bool:
		# increase each octopuses energy level by 1
		for row in map:
			for octopus in row:
				octopus.energy_level += 1
		
		# now check if any octopus has gained enough energy to flash
		high_energy_level_points = self._find_high_energy_levels(map)
		while len(high_energy_level_points) > 0:
			for high_energy_point in high_energy_level_points:
				high_energy_octopus = map[high_energy_point[1]][high_energy_point[0]]
				high_energy_octopus.has_flashed = True

				adjacent_points = self._get_adjacent_points(map, high_energy_point)
				for adjacent_point in adjacent_points:
					adjacent_octopus = map[adjacent_point[1]][adjacent_point[0]]
					adjacent_octopus.energy_level += 1

			high_energy_level_points = self._find_high_energy_levels(map)
		
		if self._did_all_octopii_flash(map):
			return True
		
		# reset flashed octopi
		for row in map:
			for octopus in row:
				if octopus.has_flashed:
					octopus.energy_level = 0
					octopus.has_flashed = False

		return False

	def part_2(self) -> int:
		map = deepcopy(self.input)
		day = 0
		all_octopii_did_flash = False
		while not all_octopii_did_flash:
			all_octopii_did_flash = self._part_2_simulate_tick(map)
			day += 1
		return day
	

	def main(self) -> None:
		print(f"1. By step 100, there had been a total of {self.part_1()} flashes")
		print(f"2. On day {self.part_2()}, all octopii flashed together")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
