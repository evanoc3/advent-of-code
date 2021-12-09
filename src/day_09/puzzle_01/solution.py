#!/usr/bin/env python3

from pathlib import Path


def parse_input(input_lines: list[str]) -> list[list[int]]:
	rows: list[list[str]] = []
	for line in [line.strip() for line in input_lines]:
		rows.append([ int(d) for d in line ])
	return rows


def get_lowest_points(height_map: list[list[int]]) -> list[tuple[int, int]]:
	local_minimums: list[tuple[int, int]] = []

	for y in range(len(height_map)):
		for x in range(len(height_map[y])):
			adjacent_values = [height_map[point[1]][point[0]] for point in get_adjacent_points(height_map, (x, y))]
			if height_map[y][x] < min(adjacent_values):
				local_minimums.append((x, y))

	return local_minimums


def get_adjacent_points(height_map: list[list[int]], point: tuple[int, int]) -> list[tuple[int, int]]:
	min_y, min_x = 0, 0
	max_y, max_x = len(height_map) - 1, len(height_map[0]) - 1

	x, y = point[0], point[1]

	adjacent_points: list[int] = []
	if y > min_y:
		adjacent_points.append(height_map[y-1][x]) # top adjacent point
	if y < max_y:
		adjacent_points.append(height_map[y+1][x]) # bottom adjacent point
	if x > min_x:
		adjacent_points.append(height_map[y][x-1]) # left adjacent point
	if x < max_x:
		adjacent_points.append(height_map[y][x+1]) # right adjacent point
	
	return adjacent_points


def get_risk_scores(height_map: list[list[int]], lowest_points: list[tuple[int, int]]) -> list[int]:
	return [ height_map[point[1]][point[0]] + 1 for point in lowest_points ]


def main() -> None:
	height_map: list[list[str]] = []
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		height_map = parse_input(input_file.readlines())
		# x,y coordinates are accessed like: height_map[y][x]
	
	local_minimums = get_lowest_points(height_map)
	risk_scores = get_risk_scores(height_map, local_minimums)

	print(f"The sum of local minimum points' risk scores is: {sum(risk_scores)}")
	return


if __name__ == "__main__":
	main()
