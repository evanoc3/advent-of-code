#pragma once

#include <vector>
#include "utils/ISolution.hpp"


namespace Year2022::Day01 {

	using Input = std::vector<std::vector<int>>;


	class Solution final : public ISolution<Input, int64_t, int64_t> {
	public:
		~Solution() = default;

		const Input getInput() const override;
		const int64_t part1(const Input input) const override;
		const int64_t part2(const Input input) const override;
	
	private:
		const int64_t sumOf(const std::vector<int> vec) const;
	};
	
}
