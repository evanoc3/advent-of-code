#!/usr/bin/env python3

from re import match
from pathlib import Path
from typing import Optional
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Instruction = tuple[str, str | int, Optional[str | int]]

	def parse_input(self, input_file_lines: list[str]) -> list[_Instruction]:
		instructions: list[Solution._Instruction] = []
		for input_line in input_file_lines:
			re_match = match(r"(\w{3}) ([wxyz])(?: ([wxyz\-0-9]+))?\n?", input_line)
			if re_match:
				assert len(re_match.groups()) == 3

				try:
					a = int(re_match.group(2))
				except:
					a = re_match.group(2)

				if re_match.group(3) is not None:
					try:
						b = int(re_match.group(3))
					except:
						b = re_match.group(3)
				else:
					b = None
					
				instructions.append((re_match.group(1), a, b))

		return instructions


	class _MonadCandidateGenerator:
		def __init__(self):
			self.counter = int("1" + "0" * 14)

		def __iter__(self):
			return self
		
		def __next__(self):
			return self.next()
		
		def next(self):
			self.counter -= 1
			while "0" in str(self.counter):
				self.counter -= 1

				if self.counter == 0:
					StopIteration()

			return self.counter

	def _validate_monad_candidate(self, monad_candidate: int, instructions: list[_Instruction]) -> bool:
		digits = [int(c) for c in str(monad_candidate)]
		assert not 0 in digits

		registers = { "w": 0, "x": 0, "y": 0, "z": 0 }
		inp_indx = 0

		for instruction, a, b in instructions:
			if instruction == "inp":
				registers[a] = digits[inp_indx]
				inp_indx += 1
			else:
				a_val = registers[a]
				b_val = registers[b] if isinstance(b, str) else b

				if instruction == "add":
					registers[a] = a_val + b_val
				elif instruction == "mul":
					registers[a] = a_val * b_val
				elif instruction == "div":
					registers[a] = int(a_val / b_val)
				elif instruction == "mod":
					registers[a] = a_val % b_val
				elif instruction == "eql":
					registers[a] = 1 if a_val == b_val else 0
				
		return registers["z"] == 0

	def part_1(self) -> int:
		for monad_candidate in Solution._MonadCandidateGenerator():
			if self._validate_monad_candidate(monad_candidate, self.input):
				return monad_candidate


	def part_2(self) -> int:
		return
	

	def main(self) -> None:
		print(f"1. The MONAD \"{self.part_1()}\" passed the validation function")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
