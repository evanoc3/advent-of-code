#pragma once

#include <vector>
#include "utils/ISolution.hpp"


namespace Year2022::Day03 {

	struct Rucksack {
		const std::vector<const char> firstCompartment;
		const std::vector<const char> secondCompartment;

		bool operator==(const Rucksack& other) const;
		const std::vector<char> contents() const;
		const bool contains(const char c) const;
	};

	using Input = std::vector<Rucksack>;


	class Solution final : public ISolution<Input, int, int> {
	public:
		~Solution() = default;

		const Input getInput() const override;
		const int part1(const Input input) const override;
		const int part2(const Input input) const override;

	private:
		const char getCommonLetter(const Rucksack rucksack) const;
		const int getLetterPriority(const char c) const;

		const char getCommonLetter(const Rucksack a, const Rucksack b, const Rucksack c) const;
	};

}
