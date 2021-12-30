#!/usr/bin/env python3

from pathlib import Path
from src.day_09.puzzle_01.solution import Map
from src.day_20.puzzle_01.solution import parse_input, pad_map, enhance_image, count_lit_pixels


def main() -> None:
	enhancement_algorithm: list[int]
	map: Map

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		enhancement_algorithm, map = parse_input(input_file.readlines())


	for i in range(50):
		map = pad_map(map, 1, 0 if i % 2 == 0 else 1)
		map = enhance_image(map, enhancement_algorithm, i)
	
	print(f"After enhancing the image {i+1} times, the number of lit pixels is: {count_lit_pixels(map)}")
	return


if __name__ == "__main__":
	main()
