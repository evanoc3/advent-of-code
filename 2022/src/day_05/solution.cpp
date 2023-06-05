#include <cctype>
#include <regex>
#include <iostream>
#include <sstream>
#include "solution.hpp"


using namespace Year2022::Day05;


Solution::Solution()
	: mInputFilePath(std::filesystem::path(__FILE__).replace_filename("input.txt")) {
}


const Input Solution::parseInput(const std::string& rawInput) const {
	std::stringstream inputStream(rawInput);
	std::string line;
	Input input;
	auto parsingInitialState{ true };
	const std::regex moveInstructionRegex(R"(move (\d+) from (\d+) to (\d+))");
	auto i{ 0 };

	while(std::getline(inputStream, line)) {
		// parsing the size of the initial state from the first line
		if(i == 0) {
			const int initialStateSize = (line.size() + 1) / 4;
			input.initialState = std::vector<std::deque<char>>(initialStateSize, std::deque<char>());
		}

		if(parsingInitialState) {
			// parsing the initial state
			if(line.size() > 0) {
				int inputColumn;
				int charIndex;
				for(charIndex = 1, inputColumn = 0; charIndex < line.size() && inputColumn < input.initialState.size(); charIndex += 4, inputColumn++) {
					if(isalpha(line.at(charIndex))) {
						input.initialState[inputColumn].push_back(line.at(charIndex));
					}
				}
			}
			// once we encounter an empty line, switch to parsing move instructions
			else {
				parsingInitialState = false;
			}
		}
		// parse move instructions
		else {
			std::smatch matches;
			if(regex_search(line, matches, moveInstructionRegex)) {
				input.moveInstructions.push_back(MoveInstruction{
					std::stoi(matches[1].str()),
					std::stoi(matches[2].str()),
					std::stoi(matches[3].str())
				});
			}
		}
		i++;
	}

	return input;
}


bool MoveInstruction::operator==(const MoveInstruction& rhs) const {
	return amount == rhs.amount &&
				 srcColumn == rhs.srcColumn &&
				 destColumn == rhs.destColumn;
}


const std::string Solution::part1(const Input& input) const {
	auto curState = input.initialState;

	for(const auto& moveInstruction : input.moveInstructions) {
		Part1::performMove(curState, moveInstruction);
	}

	return getTopOfStateColumns(curState);
}


void Solution::Part1::performMove(State& state, const MoveInstruction instruction) {
	// take the items off the source column and store them in a buffer
	std::vector<char> mvBuf;
	for(auto i = 0; i < instruction.amount; i++) {
		mvBuf.push_back( state[instruction.srcColumn - 1].front() );
		state[instruction.srcColumn - 1].pop_front();
	}

	// iterating over the buffer in reverse, add the items onto the top of the destination column
	for(auto it = mvBuf.begin(); it != mvBuf.end(); ++it) {
		state[instruction.destColumn - 1].push_front(*it);
	}
}


const std::string Solution::stateToString(const State& state) const {
	std::string stringRepr;

	for(int i = 0; i < state.size(); i++) {
		stringRepr += std::to_string(i + 1);
		stringRepr += ".";

		const auto& col = state[i];
		for(const auto& c : col) {
			stringRepr += " [";
			stringRepr += c;
			stringRepr += "]";
		}

		stringRepr += "\n";
	}

	return stringRepr;
}


const std::string Solution::moveInstructionToString(const MoveInstruction& instr) const {
	std::string stringRepr{ "Move " };
	stringRepr += std::to_string(instr.amount);
	stringRepr += " from ";
	stringRepr += std::to_string(instr.srcColumn);
	stringRepr += " to ";
	stringRepr += std::to_string(instr.destColumn);
	return stringRepr;
}


const std::string Solution::getTopOfStateColumns(const State& state) const {
	std::string tops;

	for(const auto& col : state) {
		tops += col.front();
	}

	return tops;
}


const std::string Solution::part2(const Input& input) const {
	auto curState = input.initialState;
	
	for(const auto& moveInstruction : input.moveInstructions) {
		Part2::performMove(curState, moveInstruction);
	}

	return getTopOfStateColumns(curState);
}


void Solution::Part2::performMove(State& state, const MoveInstruction instruction) {
	// take the items off the source column and store them in a buffer
	std::vector<char> mvBuf;
	for(auto i = 0; i < instruction.amount; i++) {
		mvBuf.push_back( state[instruction.srcColumn - 1].front() );
		state[instruction.srcColumn - 1].pop_front();
	}

	// iterating over the buffer in reverse, add the items onto the top of the destination column
	for(auto it = mvBuf.rbegin(); it != mvBuf.rend(); ++it) {
		state[instruction.destColumn - 1].push_front(*it);
	}
}
