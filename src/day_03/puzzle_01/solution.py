#!/usr/bin/env python3

from pathlib import Path


def parse_binary_bits_to_int(bits: list[int]) -> int:
	accumulator = 0
	for i in range(len(bits)):
		bit = bits[::-1][i]
		accumulator += bit * 2**i
	return accumulator


def get_gamma_and_epsilon_rates(diagnostic_report: list[str]) -> tuple[int, int]:
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


	return parse_binary_bits_to_int(gamma_rate_bits), parse_binary_bits_to_int(epsilon_rate_bits)



def main() -> None:
	diagnostic_report: list[str] = []

	# Read the input file
	input_file_path = Path(__file__).parent / "input.txt"
	with open(input_file_path, "r") as input_file:
		diagnostic_report = input_file.readlines()
	
	# Parse the other important numbers
	gamma_rate, epsilon_rate = get_gamma_and_epsilon_rates(diagnostic_report)

	print(f"The power consumption is: (gamma x epsilon) = ({gamma_rate} x {epsilon_rate}) = {gamma_rate * epsilon_rate}")
	return


if __name__ == "__main__":
	main()
