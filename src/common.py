from abc import ABC, abstractmethod
from typing import Any


class ISolution(ABC):

	def __init__(self, input_file_lines: list[str]):
		self.input_text = input_file_lines
		self.input = self._parse_input(input_file_lines)

	@abstractmethod
	def _parse_input(input_file_lines: list[str]) -> Any:
		pass

	@abstractmethod
	def part_1(self) -> int | str:
		pass

	@abstractmethod
	def part_2(self) -> int | str:
		pass

	@abstractmethod
	def main(self) -> None:
		pass
