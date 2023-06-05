#!/usr/bin/env python3

from collections import namedtuple
from copy import deepcopy
from pathlib import Path
from math import floor
from re import findall, match
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Input = namedtuple("Input", ["boards", "called_numbers"])

	class _Board:
		def __init__(self, numbers: list[int]):
			self.numbers = numbers
			self.marks = [
				[False for _ in range(5)],
				[False for _ in range(5)],
				[False for _ in range(5)],
				[False for _ in range(5)],
				[False for _ in range(5)],
			]
			self.last_marked_number = None

		def has(self, number: int) -> bool:
			return number in self.numbers
		
		def mark(self, number: int) -> None:
			if self.has(number):
				linear_indx = self.numbers.index(number)
				y = floor(linear_indx / 5)
				x = linear_indx % 5
				self.marks[y][x] = True
				self.last_marked_number = number
		
		def has_won(self) -> bool:
			for i in range(5):
				row = self.marks[i]
				col = [row[i] for row in self.marks]

				if all(row) or all(col):
					return True

			return False
		
		def is_number_marked(self, number: int) -> bool:
			if not self.has(number):
				return False
			
			linear_indx = self.numbers.index(number)
			y = floor(linear_indx / 5)
			x = linear_indx % 5
			is_marked = self.marks[y][x]
			return is_marked

		def calculate_score(self) -> int:
			accumulator = sum([num for num in self.numbers if not self.is_number_marked(num)])
			return accumulator * self.last_marked_number

	def _parse_input(self, input_file_lines: list[str]) -> _Input:
		call_numbers = [int(x) for x in findall(r"\d+", input_file_lines[0])]

		boards: list[Solution._Board] = []
		board_numbers: list[int] = []
		for line in input_file_lines:
			board_line_regex_match = match(r"\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\n", line)
			if board_line_regex_match:
				board_numbers.append(int(board_line_regex_match.group(1)))
				board_numbers.append(int(board_line_regex_match.group(2)))
				board_numbers.append(int(board_line_regex_match.group(3)))
				board_numbers.append(int(board_line_regex_match.group(4)))
				board_numbers.append(int(board_line_regex_match.group(5)))
			elif len(line) <= 1:
				if len(board_numbers) > 0:
					boards.append( Solution._Board(board_numbers) )
				board_numbers = []

		if len(board_numbers) > 0:
			boards.append( Solution._Board(board_numbers) )

		return Solution._Input(boards, call_numbers)


	def _get_first_winner(self, boards: list[_Board], called_numbers: list[int]) -> int:
		for number in called_numbers:
			for board in boards:
				board.mark(number)
			
			for i in range(len(boards)):
				board = boards[i]
				if board.has_won():
					return i

	def part_1(self) -> int:
		boards, called_numbers = deepcopy(self.input)
		first_winner = self._get_first_winner(boards, called_numbers)
		return boards[first_winner].calculate_score()


	def _get_last_winner(self, boards: list[_Board], called_numbers: list[int]) -> int:
		last_board_which_won = None
		boards_which_have_won = [ False for i in range(len(boards)) ]
		
		for number in called_numbers:
			for board in boards:
				board.mark(number)
			
			for i in range(len(boards)):
				board = boards[i]
				if board.has_won() and not boards_which_have_won[i]: 
					last_board_which_won = i
					boards_which_have_won[i] = True
			
			if all(boards_which_have_won):
				break

		return last_board_which_won

	def part_2(self) -> int:
		boards, called_numbers = deepcopy(self.input)
		last_winner = self._get_last_winner(boards, called_numbers)
		return boards[last_winner].calculate_score()


	def main(self) -> None:
		boards, called_numbers = deepcopy(self.input)
		first_winner = self._get_first_winner(boards, called_numbers)
		print(f"1. Board {first_winner} has won! Score: {self.part_1()}")

		boards, called_numbers = deepcopy(self.input)
		last_winner = self._get_last_winner(boards, called_numbers)
		print(f"2. The last board to win is {last_winner}. It wins with score: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
				