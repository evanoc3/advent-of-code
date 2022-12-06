#pragma once

#include <vector>
#include "utils/ISolution.hpp"



namespace Year2022::Day03 {

	struct Rucksack {
		const std::vector<const char> firstCompartment;
		const std::vector<const char> secondCompartment;

		bool operator==(const Rucksack& other) const;
	};

	using Input = std::vector<Rucksack>;


	class Solution final : public IGetInput<Input>
											 , public IPart1<Input, int> {
	public:
		~Solution() = default;

		const Input getInput() const override;
		const int part1(const Input input) const override;

	private:
		const char getCommonLetters(const Rucksack rucksack) const;
		const int getLetterPriority(const char c) const;
	};

}
