#!/usr/bin/env python3

from math import floor
from pathlib import Path
from typing import Optional
from src.day_10.puzzle_01.solution import parse_input, CorruptedChunkException, TreeNode, parse_line


def get_completion_string_for(tree: TreeNode) -> str:
	cur: Optional[TreeNode] = tree[-1] if len(tree) > 0 else None

	while cur is not None and len(cur.children) > 0 and not cur.children[-1].is_closed(): # set cur to the lower-right-most leaf node of the tree that has not been closed.
		cur = cur.children[-1]
	
	completion_string = ""

	while cur is not None:
		completion_string += get_completion_for(cur.chunk)
		cur = cur.parent

	return completion_string


def get_completion_for(opening_char: str) -> str:
	assert opening_char in "([{<"
	if opening_char == "(":
		return ")"
	elif opening_char == "[":
		return "]"
	elif opening_char == "{":
		return "}"
	else: # opening_char == "<"
		return ">"


def calculate_score_for(completion_string: str) -> int:
	accumulator = 0
	scores = { ")": 1, "]": 2, "}": 3, ">": 4 }
	for char in completion_string:
		accumulator *= 5
		assert char in ")]}>"
		accumulator += scores[char]
	return accumulator


def get_middle_score(scores: list[int]) -> int:
	assert len(scores) % 2 == 1 # scores list has an odd length (so that there is a clear middle value)
	middle_index = floor(len(scores) / 2)
	return sorted(scores)[middle_index]


def main() -> None:
	input_lines: list[str] = []

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		input_lines = parse_input(input_file.readlines())
	
	autocomplete_scores: list[int] = []

	for line in input_lines:
		tree: TreeNode
		try:
			tree = parse_line(line)
		except CorruptedChunkException as err:
			continue
		
		completion_string = get_completion_string_for(tree)
		autocomplete_scores.append( calculate_score_for(completion_string) )

	print(f"The middle value of the sorted autocomplete scores is: {get_middle_score(autocomplete_scores)}")
	return


if __name__ == "__main__":
	main()
