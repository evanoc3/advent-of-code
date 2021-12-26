#!/usr/bin/env python3

from pathlib import Path
from typing import Union


SnailFishNumberComponent = Union[int, "SnailFishNumber"]
SnailFishNumber = tuple[SnailFishNumberComponent, SnailFishNumberComponent]


def main() -> None:
	nums: list[SnailFishNumber] = []

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		nums = parse_input(input_file.readlines())
	
	sum = nums[0]
	for num in nums[1:]:
		sum = add_numbers(sum, num)
		sum = reduce_number(sum)
	
	print(f"The magnitude of the sum of the numbers is: {get_magnitude(sum)}")
	return


def parse_input(input_lines: str) -> list[SnailFishNumber]:
	nums: list[SnailFishNumber] = []

	for input_line in input_lines:
		input_line = input_line.strip()
		_, new_number = parse_number(input_line)
		nums.append(new_number)

	return nums


def parse_number(input_line: str, indx: int = 0) -> tuple[int, SnailFishNumber]:
	assert input_line[indx] == "["
	indx += 1
	
	first_item: int | SnailFishNumber
	if input_line[indx].isnumeric():
		first_item = int(input_line[indx])
	else: # input_line[indx] == "[" <- i.e. it has another SnailFishNumber as a child for the first item
		indx, first_item = parse_number(input_line, indx)
	indx += 1

	assert input_line[indx] == ","
	indx += 1

	second_item: int | SnailFishNumber
	if input_line[indx].isnumeric():
		second_item = int(input_line[indx])
	else: # input_line[indx] == "[" <- i.e. it has another SnailFishNumber as a child for the second item
		indx, second_item = parse_number(input_line, indx)
	indx += 1

	assert input_line[indx] == "]"
	return (indx, (first_item, second_item))


def add_numbers(num1: SnailFishNumber, num2: SnailFishNumber) -> SnailFishNumber:
	new_num = (num1, num2)
	return reduce_number(new_num)


def reduce_number(num: SnailFishNumber) -> SnailFishNumber:
	reduced = True
	while reduced:
		num, reduced, *_ = explode(num, 0)
		if not reduced:
			num, reduced = split(num)
	return num


def explode(num: SnailFishNumberComponent, depth: int = 0):
	if not isinstance(num, int):
		l, r = num
		if depth >= 4:
			return 0, True, l, r
		else:
			l, reduced, expl, expr = explode(l, depth + 1)
			if reduced:
				if expr != 0:
					r = _add_left(r, expr)
					expr = 0
			else:
				r, reduced, expl, expr = explode(r, depth + 1)
				if reduced:
					if expl != 0:
						l = _add_right(l, expl)
						expl = 0
			if reduced:
					return (l, r), True, expl, expr
	return num, False, 0, 0


def _add_left(n, m):
	if isinstance(n, int):
		return n + m
	else:
		a, b = n
		return _add_left(a, m), b


def _add_right(n, m):
	if isinstance(n, int):
		return n + m
	else:
		a, b = n
		return a, _add_right(b, m)


def split(num: SnailFishNumber):
	if isinstance(num, int):
		if num >= 10:
			a = num // 2
			return (a, num - a), True
	else:
		l, r = num
		l, reduced = split(l)
		if not reduced:
			r, reduced = split(r)
		if reduced:
			return (l, r), True
	return num, False


def get_magnitude(num: SnailFishNumber) -> int:
	if isinstance(num, int):
		return num
	l, r = num
	return 3 * get_magnitude(l) + 2 * get_magnitude(r)


if __name__ == "__main__":
	main()
