#pragma once

#include <vector>
#include "utils/ISolution.hpp"


namespace Year2022::Day01 {

	using Input = std::vector<std::vector<int>>;


	class Solution final : public IParseInputConst<const Input>
											 , public ISolutionWithInput<const Input&, const int64_t, const int64_t> {
	public:
		Solution();
		~Solution() = default;

		// IParseInputConst
		const Input parseInput(const std::string& rawInput) const override;

		// ISolutionWithInput
		const int64_t part1(const Input& input) const override;
		const int64_t part2(const Input& input) const override;
	
		// Public Methods
		const int64_t sumOf(const std::vector<int> vec) const;

		// Member Variables
		const std::filesystem::path mInputFilePath;
	};
	
}
