#!/usr/bin/env python3

from copy import deepcopy
from pathlib import Path
from src.year_2021.day_09.solution import Solution as Solution9
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _parse_input(self, input_file_lines: list[str]) -> Solution9.Map:
		return Solution9.parse_map_from_input(input_file_lines)


	def _get_total_risk_of_path(self, map: Solution9.Map, points: list[Solution9.Point]) -> int:
		return sum([ map[y][x] for x, y in points ])

	def _get_least_risky_path(self, map: Solution9.Map, start: Solution9.Point, end: Solution9.Point) -> list[Solution9.Point]:
		path: list[Solution9.Point] = [ start ]

		score_map = self._create_score_map(map)

		while path[-1] != end:
			adjacent_points = Solution9.get_adjacent_points(map, path[-1])
			adjacent_scores = [ score_map[y][x] for x,y in adjacent_points ]
			best_adjacent_score = min(adjacent_scores)
			best_adjacent_score_index = adjacent_scores.index(best_adjacent_score)
			best_adjacent_point = adjacent_points[best_adjacent_score_index]

			path.append(best_adjacent_point)

		return path

	def _create_score_map(self, map: Solution9.Map) -> Solution9.Map:
		score_map: Solution9.Map = [ [None] * len(map[0]) for _ in map ]
		dest = (len(map) - 1, len(map[0]) - 1)

		score_map[dest[1]][dest[0]] = map[dest[1]][dest[0]]

		frontier: list[Solution9.Point] = Solution9.get_adjacent_points(map, dest)

		while len(frontier):
			frontier_point = frontier.pop(0)
			adjacent_points = Solution9.get_adjacent_points(map, frontier_point)
			scored_neighbours = [ point for point in adjacent_points if score_map[point[1]][point[0]] is not None ]

			score_map[frontier_point[1]][frontier_point[0]] = min([score_map[y][x] for (x,y) in scored_neighbours]) + map[frontier_point[1]][frontier_point[0]]

			unscored_neighbours = [ point for point in adjacent_points if score_map[point[1]][point[0]] is None and not point in frontier ]
			frontier.extend(unscored_neighbours)

		return score_map

	def _str_path(self, path: list[Solution9.Point]) -> str:
		output = ""
		for i in range(len(path)):
			output += f"({path[i][0]},{path[i][1]})"
			if i < len(path) - 1:
				output += " -> "
		return output

	def part_1(self) -> int:
		end_point = ( len(self.input) - 1, len(self.input[0]) - 1 )
		path = self._get_least_risky_path(self.input, (0,0), end_point)
		return self._get_total_risk_of_path(self.input, path[1:])


	def _create_new_map_segment(self, map: Solution9.Map, increment: int) -> Solution9.Map:
		new_map = deepcopy(map)

		for _ in range(increment):
			for y in range(len(map)):
				for x in range(len(map[0])):
					new_map[y][x] += 1 if new_map[y][x] < 9 else 2
					new_map[y][x] %= 10
		
		return new_map

	def _expand_map(self, map: Solution9.Map) -> Solution9.Map:
		new_map = []
		for yi in range(5):
			row_segment = []

			for xi in range(5):
				i = yi + xi
				new_map_segment = self._create_new_map_segment(map, i)
				if not row_segment:
					row_segment = new_map_segment
				else: # len(row_segment) > 0
					for j in range(len(row_segment)):
						row_segment[j].extend(new_map_segment[j])

			new_map.extend(row_segment)

		return new_map

	def part_2(self) -> int:
		map = deepcopy(self.input)
		map = self._expand_map(map)

		end_point = (len(map)-1, len(map[0])-1)
		path = self._get_least_risky_path(map, (0,0), end_point)
		return self._get_total_risk_of_path(map, path[1:])
	

	def main(self) -> None:
		print(f"1. Least risky path: {self.part_1()}")
		print(f"2. The least risky path has a total risk of: {self.part_2()}")



if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()