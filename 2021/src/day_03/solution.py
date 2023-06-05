#!/usr/bin/env python3

from pathlib import Path
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _parse_input(self, input_file_lines: list[str]) -> list[str]:
		return input_file_lines


	def _bits_to_int(self, bits: list[int]) -> int:
		accumulator = 0
		for i in range(len(bits)):
			bit = bits[::-1][i]
			accumulator += bit * 2**i
		return accumulator

	def _get_gamma_and_epsilon_rates(self, diagnostic_report: list[str]) -> tuple[int, int]:
		line_length = len(diagnostic_report[0]) - 1
		gamma_rate_bits: list[int] = []
		epsilon_rate_bits: list[int] = []

		for column in range(line_length):
			ones, zeros = 0, 0
			for line in diagnostic_report:
				if line[column] == "1":
					ones += 1
				else:
					zeros += 1
			gamma_rate_bits.append(1 if ones > zeros else 0)
			epsilon_rate_bits.append(1 if ones < zeros else 0)

		return self._bits_to_int(gamma_rate_bits), self._bits_to_int(epsilon_rate_bits)

	def part_1(self) -> int:
		gamma_rate, epsilon_rate = self._get_gamma_and_epsilon_rates(self.input)
		return gamma_rate * epsilon_rate


	def _get_oxygen_generator_rating(self, diagnostic_report: list[str]) -> int:
		column = 0
		while len(diagnostic_report) > 1:
			ones, zeros = 0, 0

			for line in diagnostic_report:
				bit = line[column]
				if bit == "1":
					ones += 1
				else: # bit == 0
					zeros += 1
			
			if ones >= zeros:
				diagnostic_report = [line for line in diagnostic_report if line[column] == "1"]
			else: # ones < zeros
				diagnostic_report = [line for line in diagnostic_report if line[column] == "0"]
			
			column += 1
		
		oxygen_generator_rating_bits = [int(c) for c in diagnostic_report[0] if c in ["1", "0"]]
		return self._bits_to_int(oxygen_generator_rating_bits)

	def _get_C02_scrubber_rating(self, diagnostic_report: list[str]) -> int:
		column = 0
		while len(diagnostic_report) > 1:
			ones, zeros = 0, 0

			for line in diagnostic_report:
				bit = line[column]
				if bit == "1":
					ones += 1
				else: # bit == 0
					zeros += 1
			
			if zeros <= ones:
				diagnostic_report = [line for line in diagnostic_report if line[column] == "0"]
			else: # zeros > ones
				diagnostic_report = [line for line in diagnostic_report if line[column] == "1"]
			
			column += 1
		
		c02_scrubber_rating_bits = [int(c) for c in diagnostic_report[0] if c in ["1", "0"]]
		return self._bits_to_int(c02_scrubber_rating_bits)

	def part_2(self) -> int:
		oxygen_generator_rating = self._get_oxygen_generator_rating(self.input)
		c02_scrubber_rating = self._get_C02_scrubber_rating(self.input)
		return oxygen_generator_rating * c02_scrubber_rating


	def main(self) -> None:
		gamma, epsilon = self._get_gamma_and_epsilon_rates(self.input)
		print(f"1. The power consumption is: (gamma x epsilon) = ({gamma} x {epsilon}) = {self.part_1()}")

		oxygen = self._get_oxygen_generator_rating(self.input)
		c02 = self._get_C02_scrubber_rating(self.input)
		print(f"2. Life support rating: (O2 x CO2) = ({oxygen} x {c02}) = {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
