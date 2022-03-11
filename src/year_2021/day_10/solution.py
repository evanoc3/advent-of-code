#!/usr/bin/env python3

from math import floor
from pathlib import Path
from typing import Optional
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _parse_input(self, input_file_lines: list[str]) -> list[str]:
		return [ line.strip() for line in input_file_lines ]
	

	class _CorruptedChunkException(Exception):
		def __init__(self, message: str, corrupted_char: str):
			super().__init__(message)
			self.corrupted_char = corrupted_char

	class _TreeNode:
		def __init__(self, parent, opening_character: str):
			assert opening_character in "([{<"
			self.parent: Optional[Solution._TreeNode] = parent
			self.chunk = opening_character
			self.children: list[Solution._TreeNode] = []

		def __repr__(self) -> str:
			return f"<TreeNode val=\"{self.chunk}\", children=\"{len(self.children)}\" closed=\"{self.is_closed()}\" />"

		def close(self, closing_character: str):
			assert closing_character in ")]}>"

			if self.chunk == "(" and closing_character != ")":
				raise Solution._CorruptedChunkException(f"Expected ) but got {closing_character}", closing_character)
			elif self.chunk == "[" and closing_character != "]":
				raise Solution._CorruptedChunkException(f"Excpected ] but got {closing_character}", closing_character)
			elif self.chunk == "{" and closing_character != "}":
				raise Solution._CorruptedChunkException(f"Expected }} but got {closing_character}", closing_character)
			elif self.chunk == "<" and closing_character != ">":
				raise Solution._CorruptedChunkException(f"Expected > but got {closing_character}", closing_character)
			
			self.chunk += closing_character
		
		def is_closed(self) -> bool:
			return len(self.chunk) == 2

	def _parse_line(self, line: str) -> list[_TreeNode]:
		top_level: list[Solution._TreeNode] = []
		cur: list[Solution._TreeNode] = top_level
		parent: Optional[Solution._TreeNode] = None

		for i in range(len(line)):
			char = line[i]
			assert char in "([{<>}])"

			if char in "([{<":
				if len(cur) > 0 and not cur[-1].is_closed():
					parent = cur[-1]
					cur = parent.children
				cur.append( Solution._TreeNode(parent, char) )
			elif char in ")]}>":
				if cur[-1].is_closed():
					parent = parent.parent if parent is not None else None
					cur = parent.children if parent is not None else top_level
				cur[-1].close(char)

		return top_level

	def _get_score(self, corrupted_char: str) -> int:
		assert corrupted_char in ">}])"

		scores = {
			")": 3,
			"]": 57,
			"}": 1197,
			">": 25137
		}

		return scores[corrupted_char]

	def part_1(self) -> int:
		syntax_error_score_accumulator = 0
		for line in self.input:
			try:
				self._parse_line(line)
			except Solution._CorruptedChunkException as err:
				syntax_error_score_accumulator += self._get_score(err.corrupted_char)
		return syntax_error_score_accumulator


	def _get_completion_string_for(self, tree: _TreeNode) -> str:
		cur: Optional[Solution._TreeNode] = tree[-1] if len(tree) > 0 else None

		while cur is not None and len(cur.children) > 0 and not cur.children[-1].is_closed(): # set cur to the lower-right-most leaf node of the tree that has not been closed.
			cur = cur.children[-1]
		
		completion_string = ""

		while cur is not None:
			completion_string += self._get_completion_for(cur.chunk)
			cur = cur.parent

		return completion_string

	def _get_completion_for(self, opening_char: str) -> str:
		assert opening_char in "([{<"
		if opening_char == "(":
			return ")"
		elif opening_char == "[":
			return "]"
		elif opening_char == "{":
			return "}"
		else: # opening_char == "<"
			return ">"

	def _calculate_score_for(self, completion_string: str) -> int:
		accumulator = 0
		scores = { ")": 1, "]": 2, "}": 3, ">": 4 }
		for char in completion_string:
			accumulator *= 5
			assert char in ")]}>"
			accumulator += scores[char]
		return accumulator

	def _get_middle_score(self, scores: list[int]) -> int:
		assert len(scores) % 2 == 1 # scores list has an odd length (so that there is a clear middle value)
		middle_index = floor(len(scores) / 2)
		return sorted(scores)[middle_index]

	def part_2(self) -> int:
		autocomplete_scores: list[int] = []

		for line in self.input:
			tree: Solution._TreeNode
			try:
				tree = self._parse_line(line)
			except Solution._CorruptedChunkException:
				continue
			
			completion_string = self._get_completion_string_for(tree)
			autocomplete_scores.append( self._calculate_score_for(completion_string) )
		
		return self._get_middle_score(autocomplete_scores)


	def main(self) -> None:
		print(f"1. Total score for syntax errors: {self.part_1()}")
		print(f"2. The middle value of the sorted autocomplete scores is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
