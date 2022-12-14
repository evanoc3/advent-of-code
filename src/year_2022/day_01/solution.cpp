#include <vector>
#include <sstream>
#include "solution.hpp"


using namespace Year2022::Day01;


Solution::Solution()
	: mInputFilePath(std::filesystem::path(__FILE__).replace_filename("input.txt")) {
}


const Input Solution::parseInput(const std::string& rawInput) const {
	std::stringstream inputStream(rawInput);
	std::string line;
	Input input;
	std::vector<int> cur;

	while(std::getline(inputStream, line)) {
		if(line.length() > 0) {
			cur.push_back( std::stoi(line) );
		}
		else {
			input.push_back(cur);
			cur = std::vector<int>();
		}
	}

	if(!cur.empty()) {
		input.push_back(cur);
	}

	return input;
}


const int64_t Solution::part1(const Input& input) const {
	int64_t highest = 0;

	for(const auto& elf : input) {
		const auto elfSum = sumOf(elf);
		if(elfSum > highest) {
			highest = elfSum;
		}
	}

	return highest;
}


const int64_t Solution::sumOf(const std::vector<int> vec) const {
	int accumulator = 0;
	for(const auto& num : vec) {
		accumulator += num;
	}
	return accumulator;
}


const int64_t Solution::part2(const Input& input) const {
	int64_t highest = 0;
	int64_t secondHighest = 0;
	int64_t thirdHighest = 0;

	for(const auto& elf : input) {
		const auto elfSum = sumOf(elf);
		if(elfSum > highest) {
			thirdHighest = secondHighest;
			secondHighest = highest;
			highest = elfSum;
		}
		else if(elfSum > secondHighest) {
			thirdHighest = secondHighest;
			secondHighest = elfSum;
		}
		else if(elfSum > thirdHighest) {
			thirdHighest = elfSum;
		}
	}

	const auto sum = highest + secondHighest + thirdHighest;
	return sum;
}
