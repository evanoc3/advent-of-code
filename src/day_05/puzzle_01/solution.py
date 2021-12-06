#!/usr/bin/env python3

from pathlib import Path
from re import match


class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y


class LineSegment:
	def __init__(self, x1: int, y1: int, x2: int, y2: int):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2


def get_points(segment: LineSegment) -> list[Point]:
	points: list[Point] = []
	if segment.x1 == segment.x2:
		for y in range(min(segment.y1, segment.y2), max(segment.y1, segment.y2) + 1):
			points.append(Point(segment.x1, y))
	elif segment.y1 == segment.y2:
		for x in range(min(segment.x1, segment.x2), max(segment.x1, segment.x2) + 1):
			points.append(Point(x, segment.y1))
	return points


def get_map_size(segments: list[LineSegment]) -> tuple[int, int]:
	max_x = max([seg.x2 for seg in segments])
	max_y = max([seg.y2 for seg in segments])
	return (max_x + 1, max_y + 1)


def create_map(max_x: int, max_y: int) -> list[list[int]]:
	map = []
	for _ in range(max_y):
		map.append([0 for _ in range(max_x)])
	return map


def parse_input(lines: list[str]) -> list[LineSegment]:
	segments: list[LineSegment] = []
	for line in lines:
		segment_match = match(r"(\d+),(\d+)\s->\s(\d+),(\d+)\n", line)
		if segment_match:
			x1, y1, x2, y2 = int(segment_match.group(1)), int(segment_match.group(2)), int(segment_match.group(3)), int(segment_match.group(4))
			segments.append(LineSegment(x1, y1, x2, y2))
	return segments


def count_overlaps(map: list[list[int]]) -> int:
	double_overlaps = 0
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] >= 2:
				double_overlaps += 1
	return double_overlaps


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
