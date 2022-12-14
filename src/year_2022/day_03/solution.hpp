#pragma once

#include <vector>
#include "utils/ISolution.hpp"


namespace Year2022::Day03 {

	struct Rucksack {
	public:
		bool operator==(const Rucksack& other) const;
		const std::vector<char> contents() const;
		const bool contains(const char c) const;

		const std::vector<const char> firstCompartment;
		const std::vector<const char> secondCompartment;
	};

	using Input = std::vector<Rucksack>;


	class Solution final : public IParseInputConst<const Input>
											 , public ISolutionWithInput<const Input&, const int, const int> {
	public:
		Solution();
		~Solution() = default;

		// IParseInputConst
		const Input parseInput(const std::string& rawInput) const override;

		// ISolutionWithInput
		const int part1(const Input& input) const override;
		const int part2(const Input& input) const override;

		// Public Methods
		const char getCommonLetter(const Rucksack& rucksack) const;
		const int getLetterPriority(const char c) const;

		const char getCommonLetter(const Rucksack& a, const Rucksack& b, const Rucksack& c) const;

		// Member Variables
		const std::filesystem::path mInputFilePath;
	};

}
