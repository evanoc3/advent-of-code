#!/usr/bin/env python3

from collections import Counter, defaultdict
from itertools import product
from re import match
from pathlib import Path
from src.utils.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	def _parse_input(self, input_lines: str) -> tuple[int, int]:
		positions: list[int] = []
		for line in input_lines:
			input_re_match = match(r"Player \d starting position: (\d+)\n?", line)
			if input_re_match:
				positions.append(int(input_re_match.group(1)))
		return tuple(positions)

	class _Dice:
		def __init__(self):
			self._cur_roll = 0
			self.rolls = 0
		
		def __repr__(self) -> str:
			return f"<Dice cur={{{self._cur_roll}}} rolls={{{self.rolls}}} />"

		def roll(self) -> int:
			self._cur_roll += 1
			self._cur_roll %= 100
			if self._cur_roll == 0:
				self._cur_roll = 100

			self.rolls += 1
			return self._cur_roll

	class _Player:
		def __init__(self, id: str, position: int):
			self.id = id
			self.position = position
			self.score = 0
		
		def __repr__(self) -> str:
			return f"<Player id=\"{self.id}\" position={{{10 if self.position == 0 else self.position}}} score={{{self.score}}} />"

		def move(self, places: int) -> None:
			self.position += places
			self.position %= 10
			if self.position == 0:
				self.position = 10
			
			self.score += self.position
			return
	
	def _take_turn(self, player: _Player, dice: _Dice) -> None:
		rolls = (dice.roll(), dice.roll(), dice.roll())
		player.move(sum(rolls))
		return

	def part_1(self) -> int:
		dice = Solution._Dice()
		p1 = Solution._Player("p1", self.input[0])
		p2 = Solution._Player("p2", self.input[1])
		
		while p1.score < 1000 and p2.score < 1000:
			self._take_turn(p1, dice)
			if p1.score >= 1000:
				break
			self._take_turn(p2, dice)

		loser = p1 if p1.score < 1000 else p2
		return loser.score * dice.rolls
	

	def _p1_turn(self, universe: dict[tuple[int, int, int, int], int], move_counts: list[tuple[int, int]]) -> dict[tuple[int, int, int, int], int]:
		new_universe = defaultdict(lambda: 0)
		for ((p1_pos, p1_score, p2_pos, p2_score), possibilities_count), (move, move_count) in product(universe.items(), move_counts):
			p1_pos = ((p1_pos + move) % 10) or 10
			p1_score += p1_pos
			new_universe[(p1_pos, p1_score, p2_pos, p2_score)] += possibilities_count * move_count
		return new_universe

	def _p2_turn(self, universe: dict[tuple[int, int, int, int], int], move_counts: list[tuple[int, int]]) -> dict[tuple[int, int, int, int], int]:
		new_universe = defaultdict(lambda: 0)
		for ((p1_pos, p1_score, p2_pos, p2_score), possibilities_count), (move, move_count) in product(universe.items(), move_counts):
			p2_pos = ((p2_pos + move) % 10) or 10
			p2_score += p2_pos
			new_universe[(p1_pos, p1_score, p2_pos, p2_score)] += possibilities_count * move_count
		return new_universe

	def _remove_completed(self, universe: dict[tuple[int, int, int, int], int], completed: list[tuple[int, int, int]]):
		for k in list(universe.keys()):
			_, p1_score, _, p2_score = k
			if p1_score >= 21 or p2_score >= 21:
				completed.append((p1_score, p2_score, universe[k]))
				del universe[k]

	def part_2(self) -> int:
		possibilities = [sum(x) for x in product((1, 2, 3), repeat=3)]
		move_counts = sorted(Counter(possibilities).items())

		universe: dict[tuple[int, int, int, int], int] = {
			(self.input[0], 0, self.input[1], 0): 1
		}

		completed_possibilities: list[tuple[int, int, int]] = []

		while universe:
			universe = self._p1_turn(universe, move_counts)
			self._remove_completed(universe, completed_possibilities)
			universe = self._p2_turn(universe, move_counts)
			self._remove_completed(universe, completed_possibilities)
		
		p1_wins = sum([count for p1_score, _, count in completed_possibilities if p1_score >= 21])
		p2_wins = sum([count for _, p2_score, count in completed_possibilities if p2_score >= 21])
		return max(p1_wins, p2_wins)


	def main(self) -> None:
		print(f"1. The losing player had a score of: {self.part_1()}")
		print(f"2. The player who wins in the most universes, wins {self.part_2()} times")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
