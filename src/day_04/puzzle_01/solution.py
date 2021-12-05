#!/usr/bin/env python3

from pathlib import Path
from math import floor
from re import findall, match, Match


class Board:
	def __init__(self, numbers: list[int]):
		self.numbers = numbers
		self.marks = [
			[False for x in range(5)],
			[False for x in range(5)],
			[False for x in range(5)],
			[False for x in range(5)],
			[False for x in range(5)],
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
		

def parse_input(input: list[str]) -> tuple[list[int], list[Board]]:
	call_numbers = [int(x) for x in findall(r"\d+", input[0])]

	boards: list[Board] = []
	board_numbers: list[int] = []
	for line in input:
		board_line_regex_match = match(r"\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\n", line)
		if board_line_regex_match:
			board_numbers.append(int(board_line_regex_match.group(1)))
			board_numbers.append(int(board_line_regex_match.group(2)))
			board_numbers.append(int(board_line_regex_match.group(3)))
			board_numbers.append(int(board_line_regex_match.group(4)))
			board_numbers.append(int(board_line_regex_match.group(5)))
		elif len(line) <= 1:
			if len(board_numbers) > 0:
				boards.append( Board(board_numbers) )
			board_numbers = []
	if len(board_numbers) > 0:
		boards.append( Board(board_numbers) )
	return (call_numbers, boards)



def main() -> None:
	input_file_path = Path(__file__).parent / "input.txt"

	called_numbers: list[int]
	boards: list[Board]
	with open(input_file_path, "r") as input_file:
		called_numbers, boards = parse_input(input_file.readlines())

	for number in called_numbers:
		for board in boards:
			board.mark(number)
		
		for i in range(len(boards)):
			board = boards[i]
			if board.has_won():
				print(f"Board {i} has won on number {number}! Score: {board.calculate_score()}")
				return


if __name__ == "__main__":
	main()
