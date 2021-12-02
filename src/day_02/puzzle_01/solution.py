#!/usr/bin/env python3

from pathlib import Path
from re import match


def main() -> None:
	input_file_path = Path(__file__).parent / "input.txt"
	x, y = 0, 0

	with open(input_file_path, "r") as input_file:
		line = input_file.readline()
		while line:
			result = match(r"^(forward|up|down)\s(\d+)$", line)
			if result:
				command, magnitude = result.group(1).lower(), int(result.group(2))
				if command == "forward":
					x += magnitude
				elif command == "up":
					y -= magnitude
				elif command == "down":
					y += magnitude
			line = input_file.readline()
	print(f"The resulting vector is: (x, y) = ({x}, {y})\n                         x * y = {x * y}")
	return


if __name__ == "__main__":
	main()
