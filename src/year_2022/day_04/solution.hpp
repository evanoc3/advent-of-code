#pragma once

#include "utils/ISolution.hpp"


namespace Year2022::Day04 {

	using range = std::pair<int, int>;
	using pair = std::pair<range, range>;
	using Input = std::vector<pair>;


	class Solution final : public IGetInput<Input>
											 , public IPart1<Input, int> {
	public:
		~Solution() = default;

		const Input getInput() const override;
		const int part1(const Input input) const override;
	
	private:
		const bool rangesOverlap(range range1, range range2) const;
	};

}
