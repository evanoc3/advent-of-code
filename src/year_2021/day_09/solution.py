#!/usr/bin/env python3

from pathlib import Path
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	Map = list[list[int]]

	Point = tuple[int, int]

	@staticmethod
	def parse_map_from_input(input_file_lines: list[str]) -> Map:
		rows: Solution._Map = []
		for line in [line.strip() for line in input_file_lines]:
			rows.append([ int(d) for d in line ])
		return rows
	
	def _parse_input(self, input_file_lines: list[str]) -> Map:
		return self.parse_map_from_input(input_file_lines)


	def _get_lowest_points(self, height_map: Map) -> list[Point]:
		local_minimums: list[Solution._Point] = []

		for y in range(len(height_map)):
			for x in range(len(height_map[y])):
				adjacent_values = [height_map[point[1]][point[0]] for point in self.get_adjacent_points(height_map, (x, y))]
				if height_map[y][x] < min(adjacent_values):
					local_minimums.append((x, y))

		return local_minimums

	@staticmethod
	def get_adjacent_points(height_map: Map, point: Point) -> list[Point]:
		min_y, min_x = 0, 0
		max_y, max_x = len(height_map) - 1, len(height_map[0]) - 1

		x, y = point[0], point[1]

		adjacent_points: list[int] = []
		if y > min_y:
			adjacent_points.append((x, y-1)) # top adjacent point
		if y < max_y:
			adjacent_points.append((x, y+1)) # bottom adjacent point
		if x > min_x:
			adjacent_points.append((x-1, y)) # left adjacent point
		if x < max_x:
			adjacent_points.append((x+1, y)) # right adjacent point
		
		return adjacent_points

	def _get_risk_scores(self, height_map: Map, lowest_points: list[Point]) -> list[int]:
		return [ height_map[point[1]][point[0]] + 1 for point in lowest_points ]

	def part_1(self) -> int:
		local_minimums = self._get_lowest_points(self.input)
		risk_scores = self._get_risk_scores(self.input, local_minimums)
		return sum(risk_scores)


	class _Basin:
		def __init__(self, map: "Solution._Map", points: "list[Solution._Point]"):
			self.map = map
			self.points = points
		
		def values(self) -> list[int]:
			return [self.map[point[1]][point[0]] for point in self.points]
		
		def has(self, point: "Solution._Point") -> bool:
			return point in self.points
		
		def size(self) -> int:
			return len(self.points)

	def _create_basin(self, map: Map, minimum_point: Point) -> _Basin:
		frontier: list[Solution._Point] = [ minimum_point ]
		basin = Solution._Basin(map, [ minimum_point ])

		while len(frontier) > 0:
			search_point = frontier[0]
			del frontier[0]

			adjacent_points = self.get_adjacent_points(map, search_point)
			adjacent_values = [ map[point[1]][point[0]] for point in adjacent_points ]

			while 9 in adjacent_values:
				nine_index = adjacent_values.index(9)
				del adjacent_points[nine_index]
				del adjacent_values[nine_index]

			for adjacent_point in adjacent_points:
				if self._follow_slope(map, adjacent_point) == minimum_point and not basin.has(adjacent_point):
					basin.points.append(adjacent_point)
					frontier.append(adjacent_point)

		return basin

	def _follow_slope(self, map: Map, point: Point) -> Point:
		x, y = point[0], point[1]
		val = map[y][x]
		adjacent_points = self.get_adjacent_points(map, point)
		adjacent_values = [ map[point[1]][point[0]] for point in adjacent_points ]
		min_adjacent_value = min(adjacent_values)

		while val >= min_adjacent_value:
			point = adjacent_points[adjacent_values.index(min_adjacent_value)]
			x, y = point[0], point[1]
			val = map[y][x]
			adjacent_points = self.get_adjacent_points(map, point)
			adjacent_values = [ map[point[1]][point[0]] for point in adjacent_points ]
			min_adjacent_value = min(adjacent_values)

		return point

	def _get_largest_basins(self, basins: list[_Basin]) -> tuple[_Basin, _Basin, _Basin]:
		basins_sorted_by_size = sorted(basins, key=lambda x: x.size())
		return tuple(basins_sorted_by_size[-3:])

	def part_2(self) -> int:
		local_minimums = self._get_lowest_points(self.input)
		basins = [ self._create_basin(self.input, point) for point in local_minimums ]

		largest_basins = self._get_largest_basins(basins)

		return largest_basins[0].size() * largest_basins[1].size() * largest_basins[2].size()


	def main(self) -> None:
		print(f"1. The sum of local minimum points risk scores is: {self.part_1()}")
		print(f"2. The product of the size of the 3 largest basins is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
