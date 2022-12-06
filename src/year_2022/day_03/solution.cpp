// #include <filesystem>
// #include <vector>
// #include <iostream>
#include <filesystem>
#include <fstream>
#include "year_2022/day_03/solution.hpp"


using namespace Year2022::Day03;


const Input Solution::getInput() const {
	auto inputFilePath = std::filesystem::path(__FILE__);
	inputFilePath.replace_filename("input.txt");

	std::ifstream inputFile;
	inputFile.open(inputFilePath, std::ios::in);

	Input input;

	if(!inputFile.is_open()) {
		return input;
	}

	std::string line;
	while(getline(inputFile, line)) {
		const auto lineLength = line.size();
		
		const auto firstCompartmentStr = line.substr(0, lineLength / 2);
		const auto secondCompartmentStr = line.substr(lineLength / 2, lineLength);
		input.push_back({
			std::vector<const char>(firstCompartmentStr.begin(), firstCompartmentStr.end()),
			std::vector<const char>(secondCompartmentStr.begin(), secondCompartmentStr.end()),
		});
	}
	
	inputFile.close();
	return input;
}


bool Rucksack::operator==(const Rucksack& other) const {
	return this->firstCompartment == other.firstCompartment && this->secondCompartment == other.secondCompartment;
}


const int Solution::part1(const Input input) const {
	int accumulator = 0;
	for(const Rucksack& rucksack : input) {
		const auto commonLetter = getCommonLetters(rucksack);
		const auto commonLetterPriority = getLetterPriority(commonLetter);
		accumulator += commonLetterPriority;
	}

	return accumulator;
}


const char Solution::getCommonLetters(const Rucksack rucksack) const {
	for(const char& c1 : rucksack.firstCompartment) {
		for(const char& c2 : rucksack.secondCompartment) {
			if(c1 == c2) {
				return c1;
			}
		}
	}
	return '1';
}


const int Solution::getLetterPriority(const char c) const {
	const auto cAsciiValue = static_cast<int>(c);

	if(cAsciiValue >= 65 && cAsciiValue <= 90) { // capital letters
		return cAsciiValue - 38;
	}
	if(cAsciiValue >= 97 && cAsciiValue <= 122) { // small letters
		return cAsciiValue - 96;
	}

	return -1;
}
