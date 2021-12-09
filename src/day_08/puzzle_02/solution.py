#!/usr/bin/env python3

from enum import Enum
from pathlib import Path


def parse_input(input_lines: list[str]) -> tuple[list[str], list[str]]:
	input_patterns = [ line.split("|")[0].strip().split(" ") for line in input_lines ]
	output_patterns = [ line.split("|")[1].strip().split(" ") for line in input_lines ]
	return (input_patterns, output_patterns)



class Segment(Enum):
	TOP = "d",
	TOP_LEFT = "e"
	TOP_RIGHT = "a"
	MIDDLE = "f"
	BOTTOM_LEFT = "g"
	BOTTOM_RIGHT = "b"
	BOTTOM = "c"


def pattern_contains(pattern: str, segments: str) -> bool:
	return all([ True if seg in pattern else False for seg in segments ])


def common_segments(pattern1: str, pattern2: str) -> list[str]:
	return [ x for x in pattern1 if x in pattern2 ]


def decode_segments(input_line: list[str]) -> list[str]:
	known: dict[Segment, str] = dict()

	eight_pattern = [ pattern for pattern in input_line if len(pattern) == 7 ][0]
	seven_pattern = [ pattern for pattern in input_line if len(pattern) == 3 ][0]
	four_pattern = [ pattern for pattern in input_line if len(pattern) == 4 ][0]
	one_pattern = [ pattern for pattern in input_line if len(pattern) == 2 ][0]

	known[Segment.TOP] = [x for x in seven_pattern if x not in one_pattern][0]

	abdef_segments = four_pattern + known[Segment.TOP]

	nine_pattern = [ pattern for pattern in input_line if pattern_contains(pattern, abdef_segments) and len(pattern) == 6 ][0]

	known[Segment.BOTTOM] = [seg for seg in nine_pattern if seg not in abdef_segments][0]

	abcd_segments = one_pattern + known[Segment.TOP] + known[Segment.BOTTOM]

	three_pattern = [pattern for pattern in input_line if pattern_contains(pattern, abcd_segments) and len(pattern) == 5][0]

	known[Segment.MIDDLE] = [seg for seg in three_pattern if seg not in abcd_segments][0]

	known[Segment.TOP_LEFT] = [ seg for seg in four_pattern if seg not in three_pattern ][0]

	cefd_segments = known[Segment.BOTTOM] + known[Segment.MIDDLE] + known[Segment.TOP_LEFT] + known[Segment.TOP]
	five_pattern = [ pattern for pattern in input_line if len(common_segments(pattern, cefd_segments)) == 4 and len(pattern) == 5 ][0]

	known[Segment.BOTTOM_RIGHT] = [ seg for seg in five_pattern if seg not in cefd_segments ][0]

	known[Segment.TOP_RIGHT] = [seg for seg in one_pattern if seg != known[Segment.BOTTOM_RIGHT]][0]

	six_pattern = [ pattern for pattern in input_line if len(common_segments(pattern, five_pattern)) == 5 and len(pattern) == 6 and known[Segment.TOP_RIGHT] not in pattern ][0]

	known[Segment.BOTTOM_LEFT] = [seg for seg in six_pattern if seg not in five_pattern][0]

	zero_pattern = known[Segment.TOP] + known[Segment.TOP_RIGHT] + known[Segment.BOTTOM_RIGHT] + known[Segment.BOTTOM] + known[Segment.BOTTOM_LEFT] + known[Segment.TOP_LEFT]
	two_pattern = known[Segment.TOP] + known[Segment.TOP_RIGHT] + known[Segment.MIDDLE] + known[Segment.BOTTOM_LEFT] + known[Segment.BOTTOM]
	nine_pattern = four_pattern + known[Segment.BOTTOM] + known[Segment.TOP]

	return [
		"".join(sorted(zero_pattern)),
		"".join(sorted(one_pattern)),
		"".join(sorted(two_pattern)),
		"".join(sorted(three_pattern)), 
		"".join(sorted(four_pattern)),
		"".join(sorted(five_pattern)),
		"".join(sorted(six_pattern)),
		"".join(sorted(seven_pattern)),
		"".join(sorted(eight_pattern)),
		"".join(sorted(nine_pattern))
	]


def get_int(pattern: str, decoding: list[str]) -> int:
	matching_decoded_pattern = [decoded_pattern for decoded_pattern in decoding if len(pattern) == len(decoded_pattern) and len(common_segments(pattern, decoded_pattern)) == len(pattern)][0]
	return decoding.index(matching_decoded_pattern)



def main() -> None:
	input_lines: list[list[str]] = []

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		input_patterns, output_patterns = parse_input(input_file.readlines())

	accumulator = 0

	for i in range(len(input_patterns)):
		decoded_segments = decode_segments(input_patterns[i])

		output_digits = [get_int(pattern, decoded_segments) for pattern in output_patterns[i]]
		output_int = (output_digits[0] * 1000) + (output_digits[1] * 100) + (output_digits[2] * 10) + output_digits[3]
		accumulator += output_int
	
	print(f"The sum of all output ints is: {accumulator}")
	return


if __name__ == "__main__":
	main()
