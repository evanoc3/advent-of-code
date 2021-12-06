#!/usr/bin/env python3

from pathlib import Path
from src.day_05.puzzle_01.solution import Point, LineSegment, parse_input, get_map_size, create_map, count_overlaps


def get_points(segment: LineSegment) -> list[Point]:
	min_x, max_x = min(segment.x1, segment.x2), max(segment.x1, segment.x2)
	min_y, max_y = min(segment.y1, segment.y2), max(segment.y1, segment.y2)

	points: list[Point] = []

	if segment.x1 == segment.x2: # vertical line
		for y in range(min_y, max_y + 1):
			points.append(Point(segment.x1, y))
	elif segment.y1 == segment.y2: # horizontal line
		for x in range(min_x, max_x + 1):
			points.append(Point(x, segment.y1))
	elif max_x - min_x == max_y - min_y: # diagonal line
		delta = max_x - min_x
		x_inc = 1 if segment.x2 > segment.x1 else -1
		y_inc = 1 if segment.y2 > segment.y1 else -1
		x, y = segment.x1, segment.y1
		for _ in range(delta + 1):
			points.append(Point(x, y))
			x += x_inc
			y += y_inc
	return points


def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"
	segments: list[LineSegment] = []
	
	with open(input_file_path, "r") as input_file:
		segments = parse_input(input_file.readlines())

	map_x, map_y = get_map_size(segments)
	map = create_map(map_x, map_y)

	for segment in segments:
		for point in get_points(segment):
			map[point.y][point.x] += 1
	
	print(f"There were {count_overlaps(map)} points with 2 or more overlapping line segments")
	return


if __name__ == "__main__":
	main()
