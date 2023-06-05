#include <sstream>
#include <regex>
#include "solution.hpp"


using namespace Year2022::Day04;


Solution::Solution()
	: mInputFilePath(std::filesystem::path(__FILE__).replace_filename("input.txt")) {
}


const Input Solution::parseInput(const std::string& rawInput) const {
	std::stringstream inputStream(rawInput);
	std::string line;
	Input input;
	const std::regex inputRegex("(\\d+)-(\\d+),(\\d+)-(\\d+)");

	while(std::getline(inputStream, line)) {
		std::smatch matches;
		if(regex_search(line, matches, inputRegex)) {
			const pair newPair = {
				{ std::stoi(matches[1].str()), std::stoi(matches[2].str()) },
				{ std::stoi(matches[3].str()), std::stoi(matches[4].str()) }
			};
			input.push_back(newPair);
		}
	}
	
	return input;
}


const int Solution::part1(const Input& input) const {
	int accumulator = 0;

	for(const auto& [ range1, range2 ] : input) {
		if(rangesOverlap(range1, range2)) {
			accumulator++;
		}
	}

	return accumulator;
}


const bool Solution::rangesOverlap(const range& range1, const range& range2) const {
	return (range1.first <= range2.first && range1.second >= range2.second) || (range2.first <= range1.first && range2.second >= range1.second);
}


const int Solution::part2(const Input& input) const {
	int accumulator = 0;

	for(const auto& [ range1, range2 ] : input) {
		if(rangesIntersect(range1, range2)) {
			accumulator++;
		}
	}

	return accumulator;
}


const bool Solution::rangesIntersect(const range& range1, const range& range2) const {
	// does range2 intersect with range1
	if(range1.second < range2.first || range1.first > range2.second) {
		return false;
	}

	return true;
}
