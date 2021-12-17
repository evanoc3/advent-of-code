#!/usr/bin/env python3

from pathlib import Path


def parse_input(input_line: str):
	return hex_to_bin(input_line)


def hex_to_bin(hex_str: str) -> str:
	hex_to_bin_map = {
		"0": "0000",
		"1": "0001",
		"2": "0010",
		"3": "0011",
		"4": "0100",
		"5": "0101",
		"6": "0110",
		"7": "0111",
		"8": "1000",
		"9": "1001",
		"A": "1010",
		"B": "1011",
		"C": "1100",
		"D": "1101",
		"E": "1110",
		"F": "1111",
	}
	return "".join([hex_to_bin_map[c] for c in hex_str])


def bin_to_dec(bin_str: str) -> int:
	output = 0
	for i in range(len(bin_str)):
		c = int(bin_str[len(bin_str) - 1 - i])
		output += c * (2 ** i)
	return output


def parse(bin_str: str, indx: int = 0) -> tuple[int, int]:
	packet_version = bin_to_dec(bin_str[indx:indx+3])
	indx += 3

	packet_type_id = bin_to_dec(bin_str[indx:indx+3])
	indx += 3

	if packet_type_id == 4: # packet is a literal
		digits = ""
		while bin_str[indx] == "1":
			digits += bin_str[indx+1:indx+5]
			indx += 5
		assert bin_str[indx] == "0"
		digits += bin_str[indx+1:indx+5]
		indx += 5
	else: # packet is an operator
		length_type_id = bin_str[indx]
		indx += 1

		length_size = 11 if length_type_id == "1" else 15
		length = bin_to_dec(bin_str[indx:indx+length_size])
		indx += length_size

		while length > 0:
			subpacket_length, subpacket_version_total = parse(bin_str, indx)
			packet_version += subpacket_version_total
			subpacket_length -= indx
			indx += subpacket_length
			length -= 1 if length_type_id == "1" else subpacket_length
		
	return (indx, packet_version)


def main() -> None:
	bin_str: str

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		bin_str = parse_input(input_file.readline().strip())

	_, version_total = parse(bin_str)
	print(f"The version total is: {version_total}")
	return


if __name__ == "__main__":
	main()
