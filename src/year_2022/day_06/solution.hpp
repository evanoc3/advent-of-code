#pragma once

#include "utils/ISolution.hpp"


namespace Year2022::Day06 {

	using Input = std::string;


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
		const bool substringIsUnique(const std::string& substr) const;

		// Member Variables
		const std::filesystem::path mInputFilePath;
	};

}
