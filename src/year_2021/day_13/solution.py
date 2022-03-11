#!/usr/bin/env python3

from collections import namedtuple
from re import match
from pathlib import Path
from src.common import ISolution


input_file_path = Path(__file__).parent/ "input.txt"


class Solution(ISolution):

	_Map = list[list[bool]]

	_Input = namedtuple("Input", ["map", "fold_commands"])

	def _parse_input(self, input_file_lines: list[str]) -> _Input:
		dot_points: list[tuple[int, int]] = []
		fold_commands: list[tuple[str, int]] = []

		for line in input_file_lines:
			dot_point_re_match = match(r"(\d+),(\d+)\n?", line)
			if dot_point_re_match:
				dot_points.append((int(dot_point_re_match.group(1)), int(dot_point_re_match.group(2))))
				continue

			fold_command_re_match = match(r"fold along ([xy])=(\d+)\n?", line)
			if fold_command_re_match:
				fold_commands.append((fold_command_re_match.group(1), int(fold_command_re_match.group(2))))

		
		max_x = max([ point[0] for point in dot_points ]) + 1
		max_y = max([ point[1] for point in dot_points ]) + 1

		map: Solution._Map = []
		for y in range(max_y):
			map.append([ False for x in range(max_x) ])

		for dot_point in dot_points:
			x,y = dot_point
			map[y][x] = True

		return Solution._Input(map, fold_commands)


	def _fold(self, map: _Map, line: int) -> _Map:
		map_above_fold = map[:line]

		folded_map = map[line:][::-1]
		folded_dot_points = self._get_dot_points(folded_map)

		for folded_dot_point in folded_dot_points:
			x, y = folded_dot_point
			map_above_fold[y][x] = True

		return map_above_fold

	def _get_dot_points(self, map: _Map) -> list[tuple[int, int]]:
		points = []
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x]:
					points.append((x, y))

		return points

	def part_1(self) -> int:
		map, fold_commands = self.input
		for fold_command in fold_commands:
			axis, line = fold_command
			if axis == "y":
				map = self._fold(map, line)
			else: # axis == "x"
				inverted_map = [list(x) for x in zip(*map)]
				inverted_folded_map = self._fold(inverted_map, line)
				map = [list(x) for x in zip(*inverted_folded_map)]
			break

		return len(self._get_dot_points(map))


	def _str_map(self, map: _Map) -> None:
		map_str = ""
		for row in map:
			for col in row:
				map_str += "#" if col else "."
			map_str += "\n"
		return map_str
	
	def part_2(self) -> str:
		map, fold_commands = self.input
		for fold_command in fold_commands:
			axis, line = fold_command
			if axis == "y":
				map = self._fold(map, line)
			else: # axis == "x"
				inverted_map = [list(x) for x in zip(*map)]
				inverted_folded_map = self._fold(inverted_map, line)
				map = [list(x) for x in zip(*inverted_folded_map)]

		return self._str_map(map)

	def main(self) -> None:
		print(f"1. Total dots: {self.part_1()}")
		print(f"2. Final map:\n", self.part_2())


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
