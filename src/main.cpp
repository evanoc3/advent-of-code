#include <iostream>
#include "year_2022/day_01/solution.hpp"


int main() {
	// year 2022 day 01
	{
		const auto solution = Year2022::Day01::Solution();
		const auto input = solution.getInput();
		std::cout << "Year2022::Day01::Solution::part1(): " << solution.part1(input) << std::endl;
		std::cout << "Year2022::Day01::Solution::part2(): " << solution.part2(input) << std::endl;
	}
	
	return 0;
}
