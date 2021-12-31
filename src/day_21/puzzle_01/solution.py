#!/usr/bin/env python3

from re import match
from pathlib import Path


class Dice:
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


class Player:
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
	

def main() -> None:
	p1_pos: int
	p2_pos: int

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		p1_pos, p2_pos = parse_input(input_file.readlines())

	dice = Dice()
	p1 = Player("p1", p1_pos)
	p2 = Player("p2", p2_pos)
	
	while p1.score < 1000 and p2.score < 1000:
		take_turn(p1, dice)
		if p1.score >= 1000:
			break
		take_turn(p2, dice)

	loser = p1 if p1.score < 1000 else p2
	print(f"Player {loser.id} lost with a score of {loser.score}. The dice was rolled {dice.rolls} times. ({loser.score} x {dice.rolls}) = {loser.score * dice.rolls}")
	return


def parse_input(input_lines: str) -> tuple[int, int]:
	positions: list[int] = []
	for line in input_lines:
		input_re_match = match(r"Player \d starting position: (\d+)\n?", line)
		if input_re_match:
			positions.append(int(input_re_match.group(1)))
	return tuple(positions)


def take_turn(player: Player, dice: Dice) -> None:
	rolls = (dice.roll(), dice.roll(), dice.roll())
	player.move(sum(rolls))
	return
 


if __name__ == "__main__":
	main()
