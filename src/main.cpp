#include <iostream>
#include "year_2022/day_01/solution.hpp"
#include "year_2022/day_02/solution.hpp"
#include "year_2022/day_03/solution.hpp"
#include "year_2022/day_04/solution.hpp"
#include "year_2022/day_05/solution.hpp"


int main() {
	// year 2022 day 01
	{
		const auto solution = std::make_unique<Year2022::Day01::Solution>();
		const auto input = solution->getInput();
		std::cout << "Year2022::Day01::Solution->part1(): " << solution->part1(input) << std::endl;
		std::cout << "Year2022::Day01::Solution->part2(): " << solution->part2(input) << std::endl;
		std::cout << std::endl;
	}

	// year 2022 day 02
	{
		const auto solution = std::make_unique<Year2022::Day02::Solution>();
		const auto input = solution->getInput();
		std::cout << "Year2022::Day02::Solution->part1(): " << solution->part1(input) << std::endl;
		std::cout << "Year2022::Day02::Solution->part2(): " << solution->part2(input) << std::endl;
		std::cout << std::endl;
	}

	// year 2022 day 03
	{
		const auto solution = std::make_unique<Year2022::Day03::Solution>();
		const auto input = solution->getInput();
		std::cout << "Year2022::Day03::Solution->part1(): " << solution->part1(input) << std::endl;
		std::cout << "Year2022::Day03::Solution->part2(): " << solution->part2(input) << std::endl;
		std::cout << std::endl;
	}

	// year 2022 day 04
	{
		const auto solution = std::make_unique<Year2022::Day04::Solution>();
		const auto input = solution->getInput();
		std::cout << "Year2022::Day04::Solution->part1(): " << solution->part1(input) << std::endl;
		std::cout << "Year2022::Day04::Solution->part2(): " << solution->part2(input) << std::endl;
		std::cout << std::endl;
	}

	// year 2022 day 05
	{
		const auto solution = std::make_unique<Year2022::Day05::Solution>();
		const auto input = solution->getInput();
		std::cout << "Year2022::Day05::Solution->part1(): "  << solution->part1(input) << std::endl;
		std::cout << "Year2022::Day05::Solution->part2(): " << solution->part2(input) << std::endl;
		std::cout << std::endl;
	}

	return 0;
}
