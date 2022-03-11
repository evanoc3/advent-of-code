#!/usr/bin/env python3

from pathlib import Path
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	class _Cave:
		def __init__(self, name: str):
			self.name = name
			self.linked_caves: list[Solution._Cave] = []
		
		def is_big(self) -> bool:
			return self.name.isupper()

		def __repr__(self) -> str:
			linked_caves_str = ', '.join([ f"\"{cave.name}\"" for cave in self.linked_caves])
			return f"<Cave name=\"{self.name}\" is_big={self.is_big()} links=[{linked_caves_str}] />"

	def _parse_input(self, input_file_lines: list[str]) -> _Cave:
		cave_map: dict[str, Solution._Cave] = dict()

		for line in input_file_lines:
			cave_names = line.strip().split("-")
			if cave_names[0] not in cave_map.keys():
				cave_map[cave_names[0]] = Solution._Cave(cave_names[0])
			if cave_names[1] not in cave_map.keys():
				cave_map[cave_names[1]] = Solution._Cave(cave_names[1])
			
			if not cave_map[cave_names[1]] in cave_map[cave_names[0]].linked_caves:
				cave_map[cave_names[0]].linked_caves.append(cave_map[cave_names[1]])
			if not cave_map[cave_names[0]] in cave_map[cave_names[1]].linked_caves:
				cave_map[cave_names[1]].linked_caves.append(cave_map[cave_names[0]])

		return cave_map["start"]
		
	
	def _part_1_count_paths(self, cave: _Cave, visited: set[_Cave]) -> int:
		if cave.name == "end":
			return 1
		
		count = 0

		for linked_cave in cave.linked_caves:
			if linked_cave.is_big():
				count += self._part_1_count_paths(linked_cave, visited)
			else:
				if linked_cave not in visited:
					new_visited = visited.copy()
					new_visited.add(linked_cave)
					count += self._part_1_count_paths(linked_cave, new_visited)
		
		return count
	
	def part_1(self) -> int:
		return self._part_1_count_paths(self.input, { self.input })


	def _part_2_count_paths(self, cave: _Cave, visited: set[_Cave], visited_twice: bool) -> int:
		if cave.name == "end":
			return 1
		
		count = 0

		for linked_cave in cave.linked_caves:
			if linked_cave.is_big():
				count += self._part_2_count_paths(linked_cave, visited, visited_twice)
			elif linked_cave not in visited:
					new_visited = visited.copy()
					new_visited.add(linked_cave)
					count += self._part_2_count_paths(linked_cave, new_visited, visited_twice)
			elif visited_twice and linked_cave.name != "start":
				count += self._part_2_count_paths(linked_cave, visited, False)
		
		return count

	def part_2(self) -> int:
		return self._part_2_count_paths(self.input, { self.input }, True)

	
	def main(self) -> None:
		print(f"1. Number of paths: {self.part_1()}")
		print(f"2. Number of paths: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
	
