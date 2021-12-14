#!/usr/bin/env python3

from re import match
from pathlib import Path


def parse_input(input_lines: str) -> tuple[str, list[tuple[str, str]]]:
	polymer_template = input_lines[0].strip()

	pair_insertion_rules: list[tuple[str, str]] = []
	for input_line in input_lines[2:]:
		insertion_rule_re_match = match(r"(\w\w) -> (\w)\n?", input_line)
		if insertion_rule_re_match:
			pair_insertion_rules.append((insertion_rule_re_match.group(1), insertion_rule_re_match.group(2)))

	return (polymer_template, pair_insertion_rules)


def get_indexes(pair: str, search_str: str) -> list[int]:
	indexes: list[int] = []

	for i in range(len(search_str)-1):
		search_pair = search_str[i:i+2]
		if search_pair == pair:
			indexes.append(i)

	return indexes


def insert(c: str, s: str, i: int) -> str:
	assert i < len(s)
	return s[:i] + c + s[i:]


def apply_insertion_rules(template: str, rules: list[tuple[str, str]]) -> str:
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
		template = insert(insertion[1], template, insertion[0])

	return template


def count_gene_frequencies(template: str) -> dict[str, int]:
	frequencies: dict[str, int] = dict()

	for c in template:
		if not c in frequencies.keys():
			frequencies[c] = 1
		else: # c in frequencies.keys()
			frequencies[c] += 1

	return frequencies


def main() -> None:
	polymer_template: str
	pair_insertion_rules: list[tuple[str, str]]

	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		polymer_template, pair_insertion_rules = parse_input(input_file.readlines())
	
	for i in range(10):
		polymer_template = apply_insertion_rules(polymer_template, pair_insertion_rules)

	gene_frequencies = count_gene_frequencies(polymer_template)
	print(f"Most common frequency - least common frequency = {max(gene_frequencies.values())} - {min(gene_frequencies.values())} = {max(gene_frequencies.values()) - min(gene_frequencies.values())}")
	return


if __name__ == "__main__":
	main()
