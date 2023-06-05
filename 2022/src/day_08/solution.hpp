#pragma once

#include <vector>
#include "utils/ISolution.hpp"


namespace Year2022::Day08 {

	template<typename T>
	using Grid = std::vector<std::vector<T>>;
	
	using Input = Grid<int>;
	
	
	class Solution final : public IParseInputConst<const Input>
											 //, public ISolutionWithInput<const Input&, Part1_t, Part2_t> {
											 , public IPart1WithInput<const Input&, const int> {
	public:
		Solution();
		~Solution() = default;
		
		// IParseInputConst
		const Input parseInput(const std::string& rawInput) const override;
		
		// ISolutionWithInput
		const int part1(const Input& input) const override;
		//Part2_t part2(const Input& input) const override;
		
		// Public Methods
		int ctoi(const char& c) const;
		
		
		// Member Variables
		const std::filesystem::path mInputFilePath;
	};
	
}
