#!/usr/bin/env python3

from collections import namedtuple
from enum import Enum
from pathlib import Path
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Input = namedtuple("Input", ["input_patterns", "output_patterns"])

	def _parse_input(self, input_file_lines: list[str]) -> _Input:
		input_patterns = [ line.split("|")[0].strip().split(" ") for line in input_file_lines ]
		output_patterns = [ line.split("|")[1].strip().split(" ") for line in input_file_lines ]
		return Solution._Input(input_patterns, output_patterns)


	def _count_occurrences(self, flat_output_segments: list[list[str]]) -> dict[int, int]:
		return {
			1: len([ seg for seg in flat_output_segments if len(seg) == 2 ]),
			4: len([ seg for seg in flat_output_segments if len(seg) == 4 ]),
			7: len([ seg for seg in flat_output_segments if len(seg) == 3 ]),
			8: len([ seg for seg in flat_output_segments if len(seg) == 7 ])
		}
	
	def part_1(self) -> int:
		flat_output_segments = [item for sublist in self.input.output_patterns for item in sublist]
		occurrences = self._count_occurrences(flat_output_segments)
		return sum(occurrences.values())
	

	class _Segment(Enum):
		TOP = "d",
		TOP_LEFT = "e"
		TOP_RIGHT = "a"
		MIDDLE = "f"
		BOTTOM_LEFT = "g"
		BOTTOM_RIGHT = "b"
		BOTTOM = "c"
	
	def _pattern_contains(self, pattern: str, segments: str) -> bool:
		return all([ True if seg in pattern else False for seg in segments ])

	def _common_segments(self, pattern1: str, pattern2: str) -> list[str]:
		return [ x for x in pattern1 if x in pattern2 ]

	def _decode_segments(self, input_line: list[str]) -> list[str]:
		known: dict[Solution._Segment, str] = dict()

		eight_pattern = [ pattern for pattern in input_line if len(pattern) == 7 ][0]
		seven_pattern = [ pattern for pattern in input_line if len(pattern) == 3 ][0]
		four_pattern = [ pattern for pattern in input_line if len(pattern) == 4 ][0]
		one_pattern = [ pattern for pattern in input_line if len(pattern) == 2 ][0]

		known[Solution._Segment.TOP] = [x for x in seven_pattern if x not in one_pattern][0]

		abdef_segments = four_pattern + known[Solution._Segment.TOP]

		nine_pattern = [ pattern for pattern in input_line if self._pattern_contains(pattern, abdef_segments) and len(pattern) == 6 ][0]

		known[Solution._Segment.BOTTOM] = [seg for seg in nine_pattern if seg not in abdef_segments][0]

		abcd_segments = one_pattern + known[Solution._Segment.TOP] + known[Solution._Segment.BOTTOM]

		three_pattern = [pattern for pattern in input_line if self._pattern_contains(pattern, abcd_segments) and len(pattern) == 5][0]

		known[Solution._Segment.MIDDLE] = [seg for seg in three_pattern if seg not in abcd_segments][0]

		known[Solution._Segment.TOP_LEFT] = [ seg for seg in four_pattern if seg not in three_pattern ][0]

		cefd_segments = known[Solution._Segment.BOTTOM] + known[Solution._Segment.MIDDLE] + known[Solution._Segment.TOP_LEFT] + known[Solution._Segment.TOP]
		five_pattern = [ pattern for pattern in input_line if len(self._common_segments(pattern, cefd_segments)) == 4 and len(pattern) == 5 ][0]

		known[Solution._Segment.BOTTOM_RIGHT] = [ seg for seg in five_pattern if seg not in cefd_segments ][0]

		known[Solution._Segment.TOP_RIGHT] = [seg for seg in one_pattern if seg != known[Solution._Segment.BOTTOM_RIGHT]][0]

		six_pattern = [ pattern for pattern in input_line if len(self._common_segments(pattern, five_pattern)) == 5 and len(pattern) == 6 and known[Solution._Segment.TOP_RIGHT] not in pattern ][0]

		known[Solution._Segment.BOTTOM_LEFT] = [seg for seg in six_pattern if seg not in five_pattern][0]

		zero_pattern = known[Solution._Segment.TOP] + known[Solution._Segment.TOP_RIGHT] + known[Solution._Segment.BOTTOM_RIGHT] + known[Solution._Segment.BOTTOM] + known[Solution._Segment.BOTTOM_LEFT] + known[Solution._Segment.TOP_LEFT]
		two_pattern = known[Solution._Segment.TOP] + known[Solution._Segment.TOP_RIGHT] + known[Solution._Segment.MIDDLE] + known[Solution._Segment.BOTTOM_LEFT] + known[Solution._Segment.BOTTOM]
		nine_pattern = four_pattern + known[Solution._Segment.BOTTOM] + known[Solution._Segment.TOP]

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

	def _get_int(self, pattern: str, decoding: list[str]) -> int:
		matching_decoded_pattern = [decoded_pattern for decoded_pattern in decoding if len(pattern) == len(decoded_pattern) and len(self._common_segments(pattern, decoded_pattern)) == len(pattern)][0]
		return decoding.index(matching_decoded_pattern)

	def part_2(self) -> int:
		accumulator = 0

		for i in range(len(self.input.input_patterns)):
			decoded_segments = self._decode_segments(self.input.input_patterns[i])

			output_digits = [self._get_int(pattern, decoded_segments) for pattern in self.input.output_patterns[i]]
			output_int = (output_digits[0] * 1000) + (output_digits[1] * 100) + (output_digits[2] * 10) + output_digits[3]
			accumulator += output_int
		
		return accumulator


	def main(self) -> None:
		print(f"1. The total number of occurrences of 1,4,7,8 in the output is: {self.part_1()}")
		print(f"2. The sum of all output ints is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
