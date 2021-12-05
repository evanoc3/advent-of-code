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

	def get_points(self) -> list[Point]:
		points: list[Point] = []
		if self.x1 == self.x2:
			for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
				points.append(Point(self.x1, y))
		elif self.y1 == self.y2:
			for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
				points.append(Point(x, self.y1))
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


def main() -> None:
	input_file_path = Path(__file__).parent / "input.txt"
	segments: list[LineSegment] = []
	
	with open(input_file_path, "r") as input_file:
		line = input_file.readline()
		while line:
			segment_match = match(r"(\d+),(\d+)\s->\s(\d+),(\d+)\n", line)
			if segment_match:
				x1, y1, x2, y2 = int(segment_match.group(1)), int(segment_match.group(2)), int(segment_match.group(3)), int(segment_match.group(4))
				segments.append(LineSegment(x1, y1, x2, y2))
			line = input_file.readline()

	map_x, map_y = get_map_size(segments)
	map = create_map(map_x, map_y)

	for segment in segments:
		for point in segment.get_points():
			map[point.y][point.x] += 1
	
	double_overlaps = 0
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] >= 2:
				double_overlaps += 1
	
	print(f"There were {double_overlaps} points with 2 or more overlapping line segments")
	return


if __name__ == "__main__":
	main()
