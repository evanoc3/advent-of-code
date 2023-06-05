#include <sstream>
#include "solution.hpp"


using namespace Year2022::Day08;


Solution::Solution()
	: mInputFilePath(std::filesystem::path(__FILE__).replace_filename("input.txt")) {
}


const Input Solution::parseInput(const std::string& rawInput) const {
	std::stringstream inputStream(rawInput);
	std::string line;
	Input input;
	
	while(std::getline(inputStream, line)) {
		std::vector<int> cur( line.size() );

		for(const auto& c : line) {
			cur.push_back(ctoi(c));
		}

		input.push_back(cur);
	}
	
	return input;
}


int Solution::ctoi(const char& c) const {
	switch(c) {
		case '0':
			return 0;
		case '1':
			return 1;
		case '2':
			return 2;
		case '3':
			return 3;
		case '4':
			return 4;
		case '5':
			return 5;
		case '6':
			return 6;
		case '7':
			return 7;
		case '8':
			return 8;
		case '9':
			return 9;
	}

	return -1;
}


const int Solution::part1(const Input& input) const {
	return -1;
}


//Part2_t Solution::part2(const Input& input) const {
//}
