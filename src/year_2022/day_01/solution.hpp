#pragma once

#include <vector>
#include "utils/base_solution.hpp"


namespace Year2022::Day01 {

	using Input = std::vector<std::vector<int>>;


	class Solution final : public BaseSolution<Input, int64_t, int64_t> {
	public:
		~Solution() = default;

		Input getInput() const override;
		int64_t part1(const Input input) const override;
		int64_t part2(const Input input) const override;
	
	private:
		int64_t sumOf(std::vector<int> vec) const;
	};
	
}
