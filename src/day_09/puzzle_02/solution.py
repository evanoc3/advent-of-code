#!/usr/bin/env python3

from pathlib import Path
from src.day_09.puzzle_01.solution import Map, Point, parse_input, get_adjacent_points, get_lowest_points


class Basin:
	def __init__(self, map: Map, points: list[Point]):
		self.map = map
		self.points = points
	
	def values(self) -> list[int]:
		return [self.map[point[1]][point[0]] for point in self.points]
	
	def has(self, point: Point) -> bool:
		return point in self.points
	
	def size(self) -> int:
		return len(self.points)


def create_basin(map: Map, minimum_point: Point) -> Basin:
	frontier: list[Point] = [ minimum_point ]
	basin = Basin(map, [ minimum_point ])

	while len(frontier) > 0:
		search_point = frontier[0]
		del frontier[0]

		adjacent_points = get_adjacent_points(map, search_point)
		adjacent_values = [ map[point[1]][point[0]] for point in adjacent_points ]

		while 9 in adjacent_values:
			nine_index = adjacent_values.index(9)
			del adjacent_points[nine_index]
			del adjacent_values[nine_index]

		for adjacent_point in adjacent_points:
			if follow_slope(map, adjacent_point) == minimum_point and not basin.has(adjacent_point):
				basin.points.append(adjacent_point)
				frontier.append(adjacent_point)

	return basin


def follow_slope(map: Map, point: Point) -> Point:
	x, y = point[0], point[1]
	val = map[y][x]
	adjacent_points = get_adjacent_points(map, point)
	adjacent_values = [ map[point[1]][point[0]] for point in adjacent_points ]
	min_adjacent_value = min(adjacent_values)

	while val >= min_adjacent_value:
		point = adjacent_points[adjacent_values.index(min_adjacent_value)]
		x, y = point[0], point[1]
		val = map[y][x]
		adjacent_points = get_adjacent_points(map, point)
		adjacent_values = [ map[point[1]][point[0]] for point in adjacent_points ]
		min_adjacent_value = min(adjacent_values)

	return point


def get_largest_basins(basins: list[Basin]) -> tuple[Basin, Basin, Basin]:
	basins_sorted_by_size = sorted(basins, key=lambda x: x.size())
	return tuple(basins_sorted_by_size[-3:])


def main() -> None:
	height_map: Map = []
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		height_map = parse_input(input_file.readlines())
		# x,y coordinates are accessed like: height_map[y][x]
	
	local_minimums = get_lowest_points(height_map)
	basins = [ create_basin(height_map, point) for point in local_minimums ]

	largest_basins = get_largest_basins(basins)

	print(f"The product of the size of the 3 largest basins is: {largest_basins[0].size()} x {largest_basins[1].size()} x {largest_basins[2].size()} = {largest_basins[0].size() * largest_basins[1].size() * largest_basins[2].size()}")
	return


if __name__ == "__main__":
	main()
