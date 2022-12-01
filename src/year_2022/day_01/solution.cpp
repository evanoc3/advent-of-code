#include <iostream>
#include <filesystem>
#include <fstream>
#include "year_2022/day_01/solution.hpp"


using namespace Year2022::Day01;


Solution::Solution()
	: input( getInput() ) {
}


Input Solution::getInput() const {
	auto inputFilePath = std::filesystem::path(__FILE__);
	inputFilePath.replace_filename("input.txt");

	std::ifstream inputFile;
	inputFile.open(inputFilePath, std::ios::in);

	Input input;
	std::vector<int> cur;

	if(inputFile.is_open()) {
		std::string line;
		int lineAsInt;
		while(getline(inputFile, line)) {
			try {
				lineAsInt = std::stoi(line);
				cur.push_back(lineAsInt);
			}
			catch(const std::invalid_argument& ex) {
				input.push_back(cur);
				cur = std::vector<int>();
				continue;
			}
		}
	}
	inputFile.close();

	if(!cur.empty()) {
		input.push_back(cur);
	}
	return input;
}


int64_t Solution::part1(const Input input) const {
	int64_t highest = 0;

	for(const auto& elf : input) {
		const auto elfSum = sumOf(elf);
		if(elfSum > highest) {
			highest = elfSum;
		}
	}

	return highest;
}


int64_t Solution::sumOf(std::vector<int> vec) const {
	int accumulator = 0;
	for(const auto& num : vec) {
		accumulator += num;
	}
	return accumulator;
}


int64_t Solution::part2(const Input input) const {
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
