#include <filesystem>
#include <fstream>
#include <algorithm>
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


const int Solution::part1(const Input& input) const {
	int accumulator = 0;
	for(const Rucksack& rucksack : input) {
		const auto commonLetter = getCommonLetter(rucksack);
		const auto commonLetterPriority = getLetterPriority(commonLetter);
		accumulator += commonLetterPriority;
	}

	return accumulator;
}


const char Solution::getCommonLetter(const Rucksack rucksack) const {
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


const int Solution::part2(const Input& input) const {
	int accumulator = 0;

	for(int i = 0; i < input.size(); i += 3) {
		const auto rucksackA = input.at(i);
		const auto rucksackB = input.at(i + 1);
		const auto rucksackC = input.at(i + 2);

		const auto commonLetter = getCommonLetter(rucksackA, rucksackB, rucksackC);
		accumulator += getLetterPriority(commonLetter);
	}

	return accumulator;
}


const std::vector<char> Rucksack::contents() const {
	std::vector<char> combined( firstCompartment.size() + secondCompartment.size() );
	std::merge(firstCompartment.begin(), firstCompartment.end(), secondCompartment.begin(), secondCompartment.end(), combined.begin());
	return combined;
}


const bool Rucksack::contains(const char c) const {
	if(std::find(firstCompartment.begin(), firstCompartment.end(), c) != firstCompartment.end()) {
		return true;
	}
	if(std::find(secondCompartment.begin(), secondCompartment.end(), c) != secondCompartment.end()) {
		return true;
	}

	return false;
}


const char Solution::getCommonLetter(const Rucksack rucksackA, const Rucksack rucksackB, const Rucksack rucksackC) const {
	for(const char& c : rucksackA.contents()) {
		if(rucksackB.contains(c) && rucksackC.contains(c)) {
			return c;
		}
	}
	return '1';
}
