#!/usr/bin/env python3

from pathlib import Path
from src.day_12.puzzle_01.solution import parse_input, Cave



def count_paths(cave: Cave, visited: set[Cave], visited_twice: bool) -> int:
	if cave.name == "end":
		return 1
	
	count = 0

	for linked_cave in cave.linked_caves:
		if linked_cave.is_big():
			count += count_paths(linked_cave, visited, visited_twice)
		elif linked_cave not in visited:
				new_visited = visited.copy()
				new_visited.add(linked_cave)
				count += count_paths(linked_cave, new_visited, visited_twice)
		elif visited_twice and linked_cave.name != "start":
			count += count_paths(linked_cave, visited, False)
	
	return count


def main() -> None:
	start_cave: Cave
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		start_cave = parse_input(input_file.readlines())
	
	print(f"Number of paths: {count_paths(start_cave, {start_cave}, True)}")
	return


if __name__ == "__main__":
	main()
