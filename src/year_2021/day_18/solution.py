#!/usr/bin/env python3

from pathlib import Path
from typing import Union, Optional
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_SnailFishNumberComponent = Union[int, "_SnailFishNumber"]

	_SnailFishNumber = tuple[_SnailFishNumberComponent, _SnailFishNumberComponent]

	def _parse_number(self, input_line: str, indx: int = 0) -> tuple[int, _SnailFishNumber]:
		assert input_line[indx] == "["
		indx += 1
		
		first_item: int | Solution._SnailFishNumber
		if input_line[indx].isnumeric():
			first_item = int(input_line[indx])
		else: # input_line[indx] == "[" <- i.e. it has another SnailFishNumber as a child for the first item
			indx, first_item = self._parse_number(input_line, indx)
		indx += 1

		assert input_line[indx] == ","
		indx += 1

		second_item: int | Solution._SnailFishNumber
		if input_line[indx].isnumeric():
			second_item = int(input_line[indx])
		else: # input_line[indx] == "[" <- i.e. it has another SnailFishNumber as a child for the second item
			indx, second_item = self._parse_number(input_line, indx)
		indx += 1

		assert input_line[indx] == "]"
		return (indx, (first_item, second_item))

	def _parse_input(self, input_file_lines: list[str]) -> list[_SnailFishNumber]:
		nums: list[Solution._SnailFishNumber] = []

		for input_line in input_file_lines:
			input_line = input_line.strip()
			_, new_number = self._parse_number(input_line)
			nums.append(new_number)

		return nums


	def _add_numbers(self, num1: _SnailFishNumber, num2: _SnailFishNumber) -> _SnailFishNumber:
		new_num = (num1, num2)
		return self._reduce_number(new_num)

	def _reduce_number(self, num: _SnailFishNumber) -> _SnailFishNumber:
		reduced = True
		while reduced:
			num, reduced, *_ = self._explode(num, 0)
			if not reduced:
				num, reduced = self._split(num)
		return num

	def _explode(self, num: _SnailFishNumberComponent, depth: int = 0):
		if not isinstance(num, int):
			l, r = num
			if depth >= 4:
				return 0, True, l, r
			else:
				l, reduced, expl, expr = self._explode(l, depth + 1)
				if reduced:
					if expr != 0:
						r = self._add_left(r, expr)
						expr = 0
				else:
					r, reduced, expl, expr = self._explode(r, depth + 1)
					if reduced:
						if expl != 0:
							l = self._add_right(l, expl)
							expl = 0
				if reduced:
						return (l, r), True, expl, expr
		return num, False, 0, 0

	def _add_left(self, n, m):
		if isinstance(n, int):
			return n + m
		else:
			a, b = n
			return self._add_left(a, m), b

	def _add_right(self, n, m):
		if isinstance(n, int):
			return n + m
		else:
			a, b = n
			return a, self._add_right(b, m)

	def _split(self, num: _SnailFishNumber):
		if isinstance(num, int):
			if num >= 10:
				a = num // 2
				return (a, num - a), True
		else:
			l, r = num
			l, reduced = self._split(l)
			if not reduced:
				r, reduced = self._split(r)
			if reduced:
				return (l, r), True
		return num, False

	def _get_magnitude(self, num: _SnailFishNumber) -> int:
		if isinstance(num, int):
			return num
		l, r = num
		return 3 * self._get_magnitude(l) + 2 * self._get_magnitude(r)

	def part_1(self) -> None:
		sum = self.input[0]
		for num in self.input[1:]:
			sum = self._add_numbers(sum, num)
			sum = self._reduce_number(sum)
		return self._get_magnitude(sum)


	def part_2(self) -> int:
		highest_magnitude: Optional[int] = None
		
		for i in range(len(self.input)):
			for j in range(len(self.input)):
				if i == j:
					continue
				
				sum = self._add_numbers(self.input[i], self.input[j])
				magnitude = self._get_magnitude(sum)

				if highest_magnitude is None or magnitude > highest_magnitude:
					highest_magnitude = magnitude
		
		return highest_magnitude


	def main(self) -> None:
		print(f"1. The magnitude of the sum of the numbers is: {self.part_1()}")
		print(f"2. The highest magnitude found by adding two numbers is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
