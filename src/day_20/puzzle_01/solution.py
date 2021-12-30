#!/usr/bin/env python3

from pathlib import Path
from src.day_05.puzzle_01.solution import create_map
from src.day_09.puzzle_01.solution import Map, Point
from src.day_16.puzzle_01.solution import bin_to_dec


def main() -> None:
	enhancement_algorithm: list[int]
	map: Map

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		enhancement_algorithm, map = parse_input(input_file.readlines())

	map = pad_map(map, 2)

	for i in range(2):
		map = enhance_image(map, enhancement_algorithm, i)
	
	print(f"The number of lit pixels is: {count_lit_pixels(map)}")
	return


def parse_input(input_lines: list[str]) -> tuple[list[int], Map]:
	image_enhancement_algorithm = [ 1 if c == "#" else 0 for c in input_lines[0].strip() ]

	map: Map = []
	for row in input_lines[2:]:
		map.append([1 if c == "#" else 0 for c in row.strip()])

	return (image_enhancement_algorithm, map)


def pad_map(map: Map, padding: int, pad_value: int = 0) -> Map:
	for y in range(len(map)):
		map[y] = ([pad_value] * padding) + map[y] + ([pad_value] * padding)
	
	row_length = len(map[0])
	top_pad_rows = [ [pad_value] * row_length ] * padding
	bottom_pad_rows = [ [pad_value] * row_length ] * padding
	
	map = top_pad_rows + map + bottom_pad_rows

	return map


def get_adjacent_pixel_values(map: Map, point: Point, out_of_bounds_value: int = 0) -> list[int]:
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


def enhance_image(map: Map, algorithm: list[int], i: int) -> Map:
	new_map = create_map(len(map[0]), len(map))

	for y in range(len(map)):
		for x in range(len(map[y])):
			out_of_bounds_value = 0 if i % 2 == 0 else 1
			adjacent_pixels = "".join([str(c) for c in get_adjacent_pixel_values(map, (x, y), out_of_bounds_value)])
			adjcent_pixels_dec_value = bin_to_dec(adjacent_pixels)
			output_pixel = algorithm[adjcent_pixels_dec_value]
			new_map[y][x] = output_pixel
	return new_map


def count_lit_pixels(map: Map) -> int:
	counter = 0
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] > 0:
				counter += 1
	return counter	


if __name__ == "__main__":
	main()
