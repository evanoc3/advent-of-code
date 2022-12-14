#include <vector>
#include <algorithm>
#include "solution.hpp"


using namespace Year2022::Day06;


Solution::Solution()
	: mInputFilePath(std::filesystem::path(__FILE__).replace_filename("input.txt")) {
}


const Input Solution::parseInput(const std::string& rawInput) const {
	return rawInput;
}


const int Solution::part1(const Input& input) const {
	for(int i = 3; i < input.size(); i++) {
		auto substr = input.substr(i - 3, 4);

		if(substringIsUnique(substr)) {
			return i + 1;
		}
	}
	return -1;
}


const bool Solution::substringIsUnique(const std::string& substr) const {
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


const int Solution::part2(const Input& input) const {
		for(int i = 13; i < input.size(); i++) {
		auto substr = input.substr(i - 13, 14);

		if(substringIsUnique(substr)) {
			return i + 1;
		}
	}
	return -1;
}
