#include <filesystem>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include "solution.hpp"


using namespace Year2022::Day06;


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
	getline(inputFile, line);

	inputFile.close();
	return line;
}


const int Solution::part1(const Input input) const {
	for(int i = 3; i < input.size(); i++) {
		auto substr = input.substr(i - 3, 4);

		if(substringIsUnique(substr)) {
			return i + 1;
		}
	}
	return -1;
}


const bool Solution::substringIsUnique(const std::string substr) const {
	std::vector<char> charVec( substr.size() );

	for(auto i = 0; i < substr.size(); i++) {
		const auto c = substr.at(i);

		const auto it = std::find(charVec.begin(), charVec.end(), c);
		if(it != charVec.end()) {
			return false;
		}

		charVec.push_back( c );
	}

	return true;
} 
