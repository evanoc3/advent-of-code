#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from re import match
from pathlib import Path
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

	_Input = namedtuple("Input", ["polymer_template", "pair_insertion_rules"])

	def _parse_input(self, input_lines: str) -> _Input:
		polymer_template = input_lines[0].strip()

		pair_insertion_rules: list[tuple[str, str]] = []
		for input_line in input_lines[2:]:
			insertion_rule_re_match = match(r"(\w\w) -> (\w)\n?", input_line)
			if insertion_rule_re_match:
				pair_insertion_rules.append((insertion_rule_re_match.group(1), insertion_rule_re_match.group(2)))

		return Solution._Input(polymer_template, pair_insertion_rules)


	def _get_indexes(self, pair: str, search_str: str) -> list[int]:
		indexes: list[int] = []

		for i in range(len(search_str)-1):
			search_pair = search_str[i:i+2]
			if search_pair == pair:
				indexes.append(i)

		return indexes

	def _insert(self, c: str, s: str, i: int) -> str:
		assert i < len(s)
		return s[:i] + c + s[i:]

	def _part_1_apply_insertion_rules(self, template: str, rules: list[tuple[str, str]]) -> str:
		insertions: list[tuple[int, str]] = []

		for i in range(len(template) - 1):
			pair = template[i:i+2]
			try:
				relevant_rule_index = [rule[0] for rule in rules].index(pair)
				relevant_rule = rules[relevant_rule_index]
				insertions.append((i+1, relevant_rule[1]))
			except ValueError:
				continue
		
		# do insertions in reverse so indexes arent't affected by previous insertions
		for insertion in insertions[::-1]:
			template = self._insert(insertion[1], template, insertion[0])

		return template

	_GeneCounts = defaultdict[str, int]

	def _part_1_count_gene_frequencies(self, template: str) -> 	_GeneCounts:
		frequencies: dict[str, int] = dict()

		for c in template:
			if not c in frequencies.keys():
				frequencies[c] = 1
			else: # c in frequencies.keys()
				frequencies[c] += 1

		return frequencies

	def part_1(self) -> int:
		polymer_template = self.input.polymer_template
		for _ in range(10):
			polymer_template = self._part_1_apply_insertion_rules(polymer_template, self.input.pair_insertion_rules)

		gene_frequencies = self._part_1_count_gene_frequencies(polymer_template)
		return max(gene_frequencies.values()) - min(gene_frequencies.values())
	

	def _part_2_get_gene_frequencies(self, template: str) -> _GeneCounts:
		gene_frequencies = defaultdict(lambda: 0)
		for c in template:
			gene_frequencies[c] += 1
		return gene_frequencies

	def _get_pair_frequencies(self, template: str) -> _GeneCounts:
		pair_frequencies = defaultdict(lambda: 0)
		for i in range(len(template) - 1):
			pair = template[i:i+2]
			pair_frequencies[pair] += 1
		return pair_frequencies

	def _part_2_apply_rules(self, pair_frequencies: _GeneCounts, gene_frequencies: _GeneCounts, rules: list[tuple[str, str]]) -> tuple[_GeneCounts, _GeneCounts]:
		new_pair_frequencies = defaultdict(lambda: 0)

		for rule_pair, new_gene in rules:
			if rule_pair in pair_frequencies:
				old_pair_frequency = pair_frequencies.pop(rule_pair)

				gene_frequencies[new_gene] += old_pair_frequency

				new_pair_frequencies[rule_pair[0] + new_gene] += old_pair_frequency
				new_pair_frequencies[new_gene + rule_pair[1]] += old_pair_frequency
		
		for new_pair in new_pair_frequencies.keys():
			if new_pair_frequencies[new_pair] > 0:
				pair_frequencies[new_pair] = new_pair_frequencies[new_pair]
			else: # new_pair_frequencies[new_pair] == 0
				del new_pair_frequencies[new_pair]

		return pair_frequencies, gene_frequencies

	def part_2(self) -> int:
		pair_frequencies = self._get_pair_frequencies(self.input.polymer_template)
		gene_frequencies = self._part_2_get_gene_frequencies(self.input.polymer_template)
		
		for _ in range(40):
			pair_frequencies, gene_frequencies = self._part_2_apply_rules(pair_frequencies, gene_frequencies, self.input.pair_insertion_rules)
			assert sum([gf for gf in gene_frequencies.values()]) == sum([pf for pf in pair_frequencies.values()]) + 1
		
		sorted_gene_frequencies = sorted(gene_frequencies.items(), key=lambda x: x[1])
		return sorted_gene_frequencies[-1][1] - sorted_gene_frequencies[0][1]

	def main(self) -> None:
		print(f"1. Most common frequency - least common frequency = {self.part_1()}")
		print(f"2. Most common - least common = {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()
