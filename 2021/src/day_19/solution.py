#!/usr/bin/env python3

from collections import Counter
from itertools import product
from re import match
from pathlib import Path
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _parse_input(self, input_file_lines: list[str]) -> list[list[tuple[int, int, int]]]:
		scanner_num: int
		detected_beacons: list[list[tuple[int, int, int]]] = []

		for input_line in input_file_lines:
			scanner_line_re_match = match(r"--- scanner (\d+) ---\n?", input_line)
			if scanner_line_re_match:
				scanner_num = int(scanner_line_re_match.group(1))
				continue
			
			beacon_coords_re_match = match(r"([\-+0-9]+),([\-+0-9]+),([\-+0-9]+)", input_line)
			if beacon_coords_re_match:
				beacon_coords = (int(beacon_coords_re_match.group(1)), int(beacon_coords_re_match.group(2)), int(beacon_coords_re_match.group(3)))
				if scanner_num == len(detected_beacons):
					detected_beacons.append([beacon_coords])
				else:
					detected_beacons[scanner_num].append(beacon_coords)
		return detected_beacons


	def _get_beacons(self, detected_beacons: list[list[tuple[int, int, int]]]):
		done = set()
		next = [ detected_beacons[0] ]
		rest = detected_beacons[1:]
		shifts = [(0,0,0)]
		while next:
			aligned = next.pop()
			tmp = []
			for candidate in rest:
				r = self._try_align(aligned, candidate)
				if r:
					(updated, shift) = r
					shifts.append(shift)
					next.append(updated)
				else:
					tmp.append(candidate)
			rest = tmp
			done.update(aligned)
		return done, shifts

	def _try_align(self, aligned, candidate):
		ret = []
		dl = []
		dp = dpp = None
		for dim in range(3):
				x = [pos[dim] for pos in aligned]
				for (d,s) in [(0,1),(1,1),(2,1),(0,-1),(1,-1),(2,-1)]:
						if d == dp or d == dpp:
								continue
						t = [pos[d]*s for pos in candidate]
						w = [b-a for (a,b) in product(x, t)]
						c = Counter(w).most_common(1)
						if c[0][1] >= 12:
								break        
				if c[0][1] < 12:
						return None
				(dpp, dp) = (dp, d)
				ret.append([v - c[0][0] for v in t])
				dl.append(c[0][0])
		return (list(zip(ret[0],ret[1],ret[2])), dl)

	def part_1(self) -> int:
		beacons, _ = self._get_beacons(self.input)
		return len(beacons)
	

	def part_2(self) -> int:
		_, shifts = self._get_beacons(self.input)
		sxs = product(shifts, shifts)
		return max( sum(abs(a - b) for a, b in zip(l, r)) for l, r in sxs )


	def main(self) -> None:
		print(f"1. The number of beacons is: {self.part_1()}")
		print(f"2. The largest distance between any two scanners is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
