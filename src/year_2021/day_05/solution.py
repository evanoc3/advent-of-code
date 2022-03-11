#!/usr/bin/env python3

from collections import namedtuple
from pathlib import Path
from re import match
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Point = namedtuple("Point", ["x", "y"])

	_Map = list[list[int]]

	_LineSegment = namedtuple("LineSegment", ["x1", "y1", "x2", "y2"])

	def _get_map_size(self, segments: list[_LineSegment]) -> tuple[int, int]:
		max_x = max([seg.x2 for seg in segments])
		max_y = max([seg.y2 for seg in segments])
		return (max_x + 1, max_y + 1)

	@staticmethod
	def create_map(max_x: int, max_y: int) -> _Map:
		map = []
		for _ in range(max_y):
			map.append([0 for _ in range(max_x)])
		return map
	
	def _parse_input(self, input_file_lines: list[str]) -> list[_LineSegment]:
		segments: list[Solution._LineSegment] = []
		for line in input_file_lines:
			segment_match = match(r"(\d+),(\d+)\s->\s(\d+),(\d+)\n", line)
			if segment_match:
				x1, y1, x2, y2 = int(segment_match.group(1)), int(segment_match.group(2)), int(segment_match.group(3)), int(segment_match.group(4))
				segments.append(Solution._LineSegment(x1, y1, x2, y2))
		return segments


	def _part_1_get_points(self, segment: _LineSegment) -> list[_Point]:
		points: list[Solution._Point] = []
		if segment.x1 == segment.x2:
			for y in range(min(segment.y1, segment.y2), max(segment.y1, segment.y2) + 1):
				points.append(Solution._Point(segment.x1, y))
		elif segment.y1 == segment.y2:
			for x in range(min(segment.x1, segment.x2), max(segment.x1, segment.x2) + 1):
				points.append(Solution._Point(x, segment.y1))
		return points

	def _count_overlaps(self, map: _Map) -> int:
		double_overlaps = 0
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] >= 2:
					double_overlaps += 1
		return double_overlaps
	
	def part_1(self) -> int:
		map_x, map_y = self._get_map_size(self.input)
		map = self.create_map(map_x, map_y)

		for segment in self.input:
			for point in self._part_1_get_points(segment):
				map[point.y][point.x] += 1
		
		return self._count_overlaps(map)
	

	def _part_2_get_points(self, segment: _LineSegment) -> list[_Point]:
		min_x, max_x = min(segment.x1, segment.x2), max(segment.x1, segment.x2)
		min_y, max_y = min(segment.y1, segment.y2), max(segment.y1, segment.y2)

		points: list[Solution._Point] = []

		if segment.x1 == segment.x2: # vertical line
			for y in range(min_y, max_y + 1):
				points.append(Solution._Point(segment.x1, y))
		elif segment.y1 == segment.y2: # horizontal line
			for x in range(min_x, max_x + 1):
				points.append(Solution._Point(x, segment.y1))
		elif max_x - min_x == max_y - min_y: # diagonal line
			delta = max_x - min_x
			x_inc = 1 if segment.x2 > segment.x1 else -1
			y_inc = 1 if segment.y2 > segment.y1 else -1
			x, y = segment.x1, segment.y1
			for _ in range(delta + 1):
				points.append(Solution._Point(x, y))
				x += x_inc
				y += y_inc
		return points

	def part_2(self) -> int:
		map_x, map_y = self._get_map_size(self.input)
		map = self.create_map(map_x, map_y)

		for segment in self.input:
			for point in self._part_2_get_points(segment):
				map[point.y][point.x] += 1
		
		return self._count_overlaps(map)


	def main(self) -> None:
		print(f"1. There were {self.part_1()} points with 2 or more overlapping line segments")
		print(f"2. There were {self.part_2()} points with 2 or more overlapping line segments")



if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()