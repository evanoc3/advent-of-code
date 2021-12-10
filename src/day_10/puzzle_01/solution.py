#!/usr/bin/env python3

from pathlib import Path
from typing import Optional


def parse_input(input_lines: list[str]) -> list[str]:
	return [ line.strip() for line in input_lines ]


class CorruptedChunkException(Exception):
	def __init__(self, message: str, corrupted_char: str):
		super().__init__(message)
		self.corrupted_char = corrupted_char


class TreeNode:
	def __init__(self, parent, opening_character: str):
		assert opening_character in "([{<"
		self.parent: Optional[TreeNode] = parent
		self.chunk = opening_character
		self.children: list[TreeNode] = []

	def __repr__(self) -> str:
		return f"<TreeNode val=\"{self.chunk}\", children=\"{len(self.children)}\" closed=\"{self.is_closed()}\" />"

	def close(self, closing_character: str):
		assert closing_character in ")]}>"

		if self.chunk == "(" and closing_character != ")":
			raise CorruptedChunkException(f"Expected ) but got {closing_character}", closing_character)
		elif self.chunk == "[" and closing_character != "]":
			raise CorruptedChunkException(f"Excpected ] but got {closing_character}", closing_character)
		elif self.chunk == "{" and closing_character != "}":
			raise CorruptedChunkException(f"Expected }} but got {closing_character}", closing_character)
		elif self.chunk == "<" and closing_character != ">":
			raise CorruptedChunkException(f"Expected > but got {closing_character}", closing_character)
		
		self.chunk += closing_character
	
	def is_closed(self) -> bool:
		return len(self.chunk) == 2


def parse_line(line: str) -> list[TreeNode]:
	top_level: list[TreeNode] = []
	cur: list[TreeNode] = top_level
	parent: Optional[TreeNode] = None

	for i in range(len(line)):
		char = line[i]
		assert char in "([{<>}])"

		if char in "([{<":
			if len(cur) > 0 and not cur[-1].is_closed():
				parent = cur[-1]
				cur = parent.children
			cur.append( TreeNode(parent, char) )
		elif char in ")]}>":
			if cur[-1].is_closed():
				parent = parent.parent if parent is not None else None
				cur = parent.children if parent is not None else top_level
			cur[-1].close(char)

	return top_level


def get_score(corrupted_char: str) -> int:
	assert corrupted_char in ">}])"

	scores = {
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137
	}

	return scores[corrupted_char]


def main() -> None:
	input_lines: list[str] = []

	input_file_path = Path(__file__).parent / "input.txt"
	with open(input_file_path, "r") as input_file:
		input_lines = parse_input(input_file.readlines())
	

	syntax_error_score_accumulator = 0
	for line in input_lines:
		try:
			parse_line(line)
		except CorruptedChunkException as err:
			syntax_error_score_accumulator += get_score(err.corrupted_char)
	
	print(f"Total score for syntax errors: {syntax_error_score_accumulator}")
	return


if __name__ == "__main__":
	main()
