#!/usr/bin/env python3

from math import prod
from pathlib import Path
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _hex_to_bin(self, hex_str: str) -> str:
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

	def _parse_input(self, input_file_lines: list[str]) -> str:
		return self._hex_to_bin(input_file_lines[0].strip())


	@staticmethod
	def bin_to_dec(bin_str: str) -> int:
		output = 0
		for i in range(len(bin_str)):
			c = int(bin_str[len(bin_str) - 1 - i])
			output += c * (2 ** i)
		return output

	def _part_1_parse(self, bin_str: str, indx: int = 0) -> tuple[int, int]:
		packet_version = self.bin_to_dec(bin_str[indx:indx+3])
		indx += 3

		packet_type_id = self.bin_to_dec(bin_str[indx:indx+3])
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
			length = self.bin_to_dec(bin_str[indx:indx+length_size])
			indx += length_size

			while length > 0:
				subpacket_length, subpacket_version_total = self._part_1_parse(bin_str, indx)
				packet_version += subpacket_version_total
				subpacket_length -= indx
				indx += subpacket_length
				length -= 1 if length_type_id == "1" else subpacket_length
			
		return indx, packet_version

	def part_1(self) -> int:
		bin_str = self.input
		_, version_total = self._part_1_parse(bin_str)
		return version_total
	

	def _part_2_parse(self, bin_str: str, indx: int = 0) -> tuple[int, int]:
		indx += 3

		packet_type_id = self.bin_to_dec(bin_str[indx:indx+3])
		indx += 3

		if packet_type_id == 4: # packet is a literal
			packet_value_bits = ""
			while bin_str[indx] == "1":
				packet_value_bits += bin_str[indx+1:indx+5]
				indx += 5
			assert bin_str[indx] == "0"
			packet_value_bits += bin_str[indx+1:indx+5]
			indx += 5

			packet_value = self.bin_to_dec(packet_value_bits)
		else: # packet is an operator
			length_type_id = bin_str[indx]
			indx += 1

			length_size = 11 if length_type_id == "1" else 15
			length = self.bin_to_dec(bin_str[indx:indx+length_size])
			indx += length_size

			subpacket_values: list[int] = []

			while length > 0:
				subpacket_length, subpacket_value = self._part_2_parse(bin_str, indx)
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
			
		return indx, packet_value

	def part_2(self) -> int:
		_, packet_value = self._part_2_parse(self.input)
		return packet_value


	def main(self) -> None:
		print(f"1. The version total is: {self.part_1()}")
		print(f"2. The value of the outer-most packet is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
