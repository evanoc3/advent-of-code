#!/usr/bin/env python3

from pathlib import Path
from src.day_09.puzzle_01.solution import Map, Point, get_adjacent_points, parse_input


def get_total_risk_of_path(map: Map, points: list[Point]) -> int:
	return sum([ map[y][x] for (x,y) in points ])


def get_least_risky_path(map: Map, start: Point, end: Point) -> list[Point]:
	path: list[Point] = [ start ]

	score_map = create_score_map(map)

	while path[-1] != end:
		adjacent_points = get_adjacent_points(map, path[-1])
		adjacent_scores = [ score_map[y][x] for x,y in adjacent_points ]
		best_adjacent_score = min(adjacent_scores)
		best_adjacent_score_index = adjacent_scores.index(best_adjacent_score)
		best_adjacent_point = adjacent_points[best_adjacent_score_index]

		path.append(best_adjacent_point)

	return path


def create_score_map(map: Map) -> Map:
	score_map: Map = [ [None] * len(map[0]) for row in map ]
	dest = (len(map) - 1, len(map[0]) - 1)

	score_map[dest[1]][dest[0]] = map[dest[1]][dest[0]]

	frontier: list[Point] = get_adjacent_points(map, dest)

	while len(frontier):
		frontier_point = frontier.pop(0)
		adjacent_points = get_adjacent_points(map, frontier_point)
		scored_neighbours = [ point for point in adjacent_points if score_map[point[1]][point[0]] is not None ]

		score_map[frontier_point[1]][frontier_point[0]] = min([score_map[y][x] for (x,y) in scored_neighbours]) + map[frontier_point[1]][frontier_point[0]]

		unscored_neighbours = [ point for point in adjacent_points if score_map[point[1]][point[0]] is None and not point in frontier ]
		frontier.extend(unscored_neighbours)

	return score_map


def print_path(path) -> str:
	output = ""
	for i in range(len(path)):
		output += f"({path[i][0]},{path[i][1]})"
		if i < len(path) - 1:
			output += " -> "
	return output


def main() -> None:
	map: Map
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		map = parse_input(input_file.readlines())

	end_point = (len(map)-1, len(map[0])-1)
	path = get_least_risky_path(map, (0,0), end_point)
	print(f"Least risky path ({get_total_risk_of_path(map, path[1:])}): {print_path(path)}")
	return


if __name__ == "__main__":
	main()
