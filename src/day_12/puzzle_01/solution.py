#!/usr/bin/env python3

from pathlib import Path


class Cave:
	def __init__(self, name: str):
		self.name = name
		self.linked_caves: list[Cave] = []
	
	def is_big(self) -> bool:
		return self.name.isupper()

	
	def __repr__(self) -> str:
		linked_caves_str = ', '.join([ f"\"{cave.name}\"" for cave in self.linked_caves])
		return f"<Cave name=\"{self.name}\" is_big={self.is_big()} links=[{linked_caves_str}] />"


def parse_input(input_lines: str) -> Cave:
	cave_map: dict[str, Cave] = dict()

	for line in input_lines:
		cave_names = line.strip().split("-")
		if cave_names[0] not in cave_map.keys():
			cave_map[cave_names[0]] = Cave(cave_names[0])
		if cave_names[1] not in cave_map.keys():
			cave_map[cave_names[1]] = Cave(cave_names[1])
		
		if not cave_map[cave_names[1]] in cave_map[cave_names[0]].linked_caves:
			cave_map[cave_names[0]].linked_caves.append(cave_map[cave_names[1]])
		if not cave_map[cave_names[0]] in cave_map[cave_names[1]].linked_caves:
			cave_map[cave_names[1]].linked_caves.append(cave_map[cave_names[0]])

	return cave_map["start"]


def count_paths(cave: Cave, visited: set[Cave]) -> int:
	if cave.name == "end":
		return 1
	
	count = 0

	for linked_cave in cave.linked_caves:
		if linked_cave.is_big():
			count += count_paths(linked_cave, visited)
		else:
			if linked_cave not in visited:
				new_visited = visited.copy()
				new_visited.add(linked_cave)
				count += count_paths(linked_cave, new_visited)
	
	return count


def main() -> None:
	start_cave: Cave
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		start_cave = parse_input(input_file.readlines())
	
	print(f"Number of paths: {count_paths(start_cave, [ start_cave ])}")
	return


if __name__ == "__main__":
	main()
