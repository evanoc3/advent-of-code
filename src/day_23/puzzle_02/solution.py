#!/usr/bin/env python3

from pathlib import Path
from src.day_23.puzzle_01.solution import parse_input, check_state


def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		data = parse_input(input_file.readlines())
	
	print(f"2. The least energy required is: {check_state(extend(data), {})}")
	return

def extend(state):
  return (*state[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *state[3:],)


if __name__ == "__main__":
	main()
