#!/usr/bin/env python3

from collections import namedtuple
from pathlib import Path
from src.day_05.solution import Solution as Solution5
from src.day_09.solution import Solution as Solution9
from src.day_16.solution import Solution as Solution16
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Input = namedtuple("Input", ["enhancement_algorithm", "map"])

	def _parse_input(self, input_file_lines: list[str]) -> _Input:
		image_enhancement_algorithm = [ 1 if c == "#" else 0 for c in input_file_lines[0].strip() ]

		map: Solution9.Map = []
		for row in input_file_lines[2:]:
			map.append([1 if c == "#" else 0 for c in row.strip()])

		return Solution._Input(image_enhancement_algorithm, map)


	def _pad_map(self, map: Solution9.Map, padding: int, pad_value: int = 0) -> Solution5._Map:
		for y in range(len(map)):
			map[y] = ([pad_value] * padding) + map[y] + ([pad_value] * padding)
		
		row_length = len(map[0])
		top_pad_rows = [ [pad_value] * row_length ] * padding
		bottom_pad_rows = [ [pad_value] * row_length ] * padding
		
		map = top_pad_rows + map + bottom_pad_rows

		return map

	def _enhance_image(self, map: Solution9.Map, algorithm: list[int], i: int) -> Solution9.Map:
		new_map = Solution5.create_map(len(map[0]), len(map))

		for y in range(len(map)):
			for x in range(len(map[y])):
				out_of_bounds_value = 0 if i % 2 == 0 else 1
				adjacent_pixels = "".join([str(c) for c in self._get_adjacent_pixel_values(map, (x, y), out_of_bounds_value)])
				adjcent_pixels_dec_value = Solution16.bin_to_dec(adjacent_pixels)
				output_pixel = algorithm[adjcent_pixels_dec_value]
				new_map[y][x] = output_pixel
		return new_map

	def _get_adjacent_pixel_values(self, map: Solution9.Map, point: Solution9.Point, out_of_bounds_value: int = 0) -> list[int]:
		min_y, min_x = 0, 0
		max_y, max_x = len(map) - 1, len(map[0]) - 1

		x, y = point

		has_top, has_bottom = y > min_y, y < max_y
		has_left, has_right = x > min_x, x < max_x

		adjacent_pixel_values: list[int] = []

		adjacent_pixel_values.append(map[y-1][x-1] if has_top and has_left else out_of_bounds_value) # top-left adjacent point
		adjacent_pixel_values.append(map[y-1][x] if has_top else out_of_bounds_value) # top adjacent point
		adjacent_pixel_values.append(map[y-1][x+1] if has_top and has_right else out_of_bounds_value) # top-right adjacent point
		adjacent_pixel_values.append(map[y][x-1] if has_left else out_of_bounds_value) # left adjacent point
		adjacent_pixel_values.append(map[y][x]) # central point
		adjacent_pixel_values.append(map[y][x+1] if has_right else out_of_bounds_value) # right adjacent point
		adjacent_pixel_values.append(map[y+1][x-1] if has_bottom and has_left else out_of_bounds_value) # bottom-left adjacent point
		adjacent_pixel_values.append(map[y+1][x] if has_bottom else out_of_bounds_value) # bottom adjacent point
		adjacent_pixel_values.append(map[y+1][x+1] if has_bottom and has_right else out_of_bounds_value) # bottom-right adjacent point
		
		return adjacent_pixel_values

	def _count_lit_pixels(self, map: Solution9.Map) -> int:
		counter = 0
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] > 0:
					counter += 1
		return counter	

	def part_1(self) -> None:
		map = self._pad_map(self.input.map, 2)

		for i in range(2):
			map = self._enhance_image(map, self.input.enhancement_algorithm, i)
		
		return self._count_lit_pixels(map)
	

	def part_2(self) -> int:
		map = self.input.map
		for i in range(50):
			map = self._pad_map(map, 1, 0 if i % 2 == 0 else 1)
			map = self._enhance_image(map, self.input.enhancement_algorithm, i)
		
		return self._count_lit_pixels(map)


	def main(self) -> None:
		print(f"1. The number of lit pixels is: {self.part_1()}")
		print(f"2. After enhancing the image 50 times, the number of lit pixels is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
