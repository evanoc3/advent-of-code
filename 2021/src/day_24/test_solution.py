#!/usr/bin/env python3

from unittest import TestCase, main, skip
from src.day_24.solution import input_file_path, Solution


class Day24SolutionTest(TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		with open(input_file_path, "r") as input_file:
			cls.input = input_file.readlines()

	def setUp(self) -> None:
		self.solution = Solution(self.__class__.input)
	
	def tearDown(self) -> None:
		self.solution = None

	@skip
	def test_part_1(self):
		self.assertEqual(self.solution.part_1(), 0)
	
	@skip
	def test_part_2(self):
		self.assertEqual(self.solution.part_2(), 0)


if __name__ == "__main__":
	main()
