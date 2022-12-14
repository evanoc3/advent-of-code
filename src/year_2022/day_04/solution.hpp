#pragma once

#include <utility>
#include "utils/ISolution.hpp"


namespace Year2022::Day04 {

	using range = std::pair<int, int>;
	using pair = std::pair<range, range>;
	using Input = std::vector<pair>;


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
		const bool rangesOverlap(const range& range1, const range& range2) const;
		const bool rangesIntersect(const range& range1, const range& range2) const;

		// Member Variables
		const std::filesystem::path mInputFilePath;
	};

}
