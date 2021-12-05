#!/usr/bin/env python3

from pathlib import Path
from src.day_04.puzzle_01.solution import Board, parse_input


def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		called_numbers, boards = parse_input(input_file.readlines())
	
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

	
	if last_board_which_won:
		print(f"The last board which will win is {last_board_which_won}. It wins with score: {boards[last_board_which_won].calculate_score()}")
	return


if __name__ == "__main__":
	main()
