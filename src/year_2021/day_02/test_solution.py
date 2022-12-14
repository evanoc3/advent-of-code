#!/usr/bin/env python3

from unittest import TestCase, main
from src.year_2021.day_02.solution import input_file_path, Solution


class Day2SolutionTest(TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		with open(input_file_path, "r") as input_file:
			cls.input = input_file.readlines()

	def setUp(self) -> None:
		self.solution = Solution(self.__class__.input)
	
	def tearDown(self) -> None:
		self.solution = None


	def test_part_1(self):
		self.assertEqual(self.solution.part_1(), 1855814)
	
	def test_part_2(self):
		self.assertEqual(self.solution.part_2(), 1845455714)


if __name__ == "__main__":
	main()
