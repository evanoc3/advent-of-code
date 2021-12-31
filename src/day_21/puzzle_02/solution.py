#!/usr/bin/env python3

from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
from src.day_21.puzzle_01.solution import parse_input


def main() -> None:
	p1_pos: int
	p2_pos: int

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		p1_pos, p2_pos = parse_input(input_file.readlines())
	
	possibilities = [sum(x) for x in product((1, 2, 3), repeat=3)]
	move_counts = sorted(Counter(possibilities).items())

	universe: dict[tuple[int, int, int, int], int] = {
		(p1_pos, 0, p2_pos, 0): 1
	}

	completed_possibilities: list[tuple[int, int, int]] = []

	while universe:
		universe = p1_turn(universe, move_counts)
		remove_completed(universe, completed_possibilities)
		universe = p2_turn(universe, move_counts)
		remove_completed(universe, completed_possibilities)
	
	p1_wins = sum([count for p1_score, _, count in completed_possibilities if p1_score >= 21])
	p2_wins = sum([count for _, p2_score, count in completed_possibilities if p2_score >= 21])
	print(f"The player who wins in the most universes, wins {max(p1_wins, p2_wins)} times")
	return


def p1_turn(universe: dict[tuple[int, int, int, int], int], move_counts: list[tuple[int, int]]) -> dict[tuple[int, int, int, int], int]:
	new_universe = defaultdict(lambda: 0)
	for ((p1_pos, p1_score, p2_pos, p2_score), possibilities_count), (move, move_count) in product(universe.items(), move_counts):
		p1_pos = ((p1_pos + move) % 10) or 10
		p1_score += p1_pos
		new_universe[(p1_pos, p1_score, p2_pos, p2_score)] += possibilities_count * move_count
	return new_universe

def p2_turn(universe: dict[tuple[int, int, int, int], int], move_counts: list[tuple[int, int]]) -> dict[tuple[int, int, int, int], int]:
	new_universe = defaultdict(lambda: 0)
	for ((p1_pos, p1_score, p2_pos, p2_score), possibilities_count), (move, move_count) in product(universe.items(), move_counts):
		p2_pos = ((p2_pos + move) % 10) or 10
		p2_score += p2_pos
		new_universe[(p1_pos, p1_score, p2_pos, p2_score)] += possibilities_count * move_count
	return new_universe

def remove_completed(universe: dict[tuple[int, int, int, int], int], completed: list[tuple[int, int, int]]):
	for k in list(universe.keys()):
		_, p1_score, _, p2_score = k
		if p1_score >= 21 or p2_score >= 21:
			completed.append((p1_score, p2_score, universe[k]))
			del universe[k]

if __name__ == "__main__":
	main()
