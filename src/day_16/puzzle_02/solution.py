#!/usr/bin/env python3

from math import prod
from pathlib import Path
from src.day_16.puzzle_01.solution import parse_input, bin_to_dec


def parse(bin_str: str, indx: int = 0) -> tuple[int, int]:
	packet_version = bin_to_dec(bin_str[indx:indx+3])
	indx += 3

	packet_type_id = bin_to_dec(bin_str[indx:indx+3])
	indx += 3

	if packet_type_id == 4: # packet is a literal
		packet_value_bits = ""
		while bin_str[indx] == "1":
			packet_value_bits += bin_str[indx+1:indx+5]
			indx += 5
		assert bin_str[indx] == "0"
		packet_value_bits += bin_str[indx+1:indx+5]
		indx += 5

		packet_value = bin_to_dec(packet_value_bits)
	else: # packet is an operator
		length_type_id = bin_str[indx]
		indx += 1

		length_size = 11 if length_type_id == "1" else 15
		length = bin_to_dec(bin_str[indx:indx+length_size])
		indx += length_size

		subpacket_values: list[int] = []

		while length > 0:
			subpacket_length, subpacket_value = parse(bin_str, indx)
			subpacket_values.append(subpacket_value)
			subpacket_length -= indx
			indx += subpacket_length
			length -= 1 if length_type_id == "1" else subpacket_length

		if packet_type_id == 0: # sum operator
			packet_value = sum(subpacket_values)
		elif packet_type_id == 1: # product operator
			packet_value = prod(subpacket_values)
		elif packet_type_id == 2: # minimum operator
			packet_value = min(subpacket_values)
		elif packet_type_id == 3: # maximum operator
			packet_value = max(subpacket_values)
		elif packet_type_id == 5: # greater-than operator
			assert len(subpacket_values) == 2
			packet_value = 1 if subpacket_values[0] > subpacket_values[1] else 0
		elif packet_type_id == 6: # less-than operator
			assert len(subpacket_values) == 2
			packet_value = 1 if subpacket_values[0] < subpacket_values[1] else 0
		elif packet_type_id == 7: # equal-to operator
			assert len(subpacket_values) == 2
			packet_value = 1 if subpacket_values[0] == subpacket_values[1] else 0
		
	return (indx, packet_value)


def main() -> None:
	bin_str: str

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		bin_str = parse_input(input_file.readline().strip())

	_, packet_value = parse(bin_str)
	print(f"The value of the outer-most packet is: {packet_value}")
	return


if __name__ == "__main__":
	main()
