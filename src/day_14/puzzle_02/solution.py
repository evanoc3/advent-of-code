#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path
from src.day_14.puzzle_01.solution import parse_input


def get_gene_frequencies(template: str) -> defaultdict[str, int]:
	gene_frequencies = defaultdict(lambda: 0)
	for c in template:
		gene_frequencies[c] += 1
	return gene_frequencies


def get_pair_frequencies(template: str) -> defaultdict[str, int]:
	pair_frequencies = defaultdict(lambda: 0)
	for i in range(len(template) - 1):
		pair = template[i:i+2]
		pair_frequencies[pair] += 1
	return pair_frequencies


def apply_rules(pair_frequencies: defaultdict[str, int], gene_frequencies: defaultdict[str, int], rules: list[tuple[str, str]]) -> tuple[defaultdict[str, int], defaultdict[str, int]]:
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


def main() -> None:
	polymer_template: str
	pair_insertion_rules: list[tuple[str, str]]

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		polymer_template, pair_insertion_rules = parse_input(input_file.readlines())
	
	pair_frequencies = get_pair_frequencies(polymer_template)
	gene_frequencies = get_gene_frequencies(polymer_template)
	
	for _ in range(40):
		pair_frequencies, gene_frequencies = apply_rules(pair_frequencies, gene_frequencies, pair_insertion_rules)
		assert sum([gf for gf in gene_frequencies.values()]) == sum([pf for pf in pair_frequencies.values()]) + 1
	
	sorted_gene_frequencies = sorted(gene_frequencies.items(), key=lambda x: x[1])
	print(f"Most common - least common = {sorted_gene_frequencies[-1][1]} ({sorted_gene_frequencies[-1][0]}) - {sorted_gene_frequencies[0][1]} ({sorted_gene_frequencies[0][0]}) = {sorted_gene_frequencies[-1][1] - sorted_gene_frequencies[0][1]}")
	return


if __name__ == "__main__":
	main()