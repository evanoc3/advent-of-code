#include <filesystem>
#include <fstream>
#include <regex>
#include "year_2022/day_04/solution.hpp"


using namespace Year2022::Day04;


const Input Solution::getInput() const {
	auto inputFilePath = std::filesystem::path(__FILE__);
	inputFilePath.replace_filename("input.txt");

	std::ifstream inputFile;
	inputFile.open(inputFilePath, std::ios::in);

	Input input;

	if(!inputFile.is_open()) {
		return input;
	}

	const std::regex inputRegex("(\\d+)-(\\d+),(\\d+)-(\\d+)");

	std::string line;
	while(getline(inputFile, line)) {

		std::smatch matches;
		if(regex_search(line, matches, inputRegex)) {
			const pair newPair = {
				{ std::stoi(matches[1].str()), std::stoi(matches[2].str()) },
				{ std::stoi(matches[3].str()), std::stoi(matches[4].str()) }
			};
			input.push_back(newPair);
		}
	}
	
	inputFile.close();
	return input;
}


const int Solution::part1(const Input input) const {
	int accumulator = 0;

	for(const auto& [ range1, range2 ] : input) {
		if(rangesOverlap(range1, range2)) {
			accumulator++;
		}
	}

	return accumulator;
}


const bool Solution::rangesOverlap(range range1, range range2) const {
	return (range1.first <= range2.first && range1.second >= range2.second) || (range2.first <= range1.first && range2.second >= range1.second);
}
