#include <iostream>
#include <filesystem>
#include <fstream>
#include "year_2022/day_02/solution.hpp"


using namespace Year2022::Day02;


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
		if(line.length() != 3) {
			continue;
		}

		const auto opponentPlay = decryptPlay(line.at(0));
		const auto yourPlay = decryptPlay(line.at(2));

		if(opponentPlay != RockPaperScissorsPlay::Invalid && yourPlay != RockPaperScissorsPlay::Invalid) {
		const auto pair = std::pair<const RockPaperScissorsPlay, const RockPaperScissorsPlay>(opponentPlay, yourPlay);
		input.push_back(pair);
		}

	}
	
	inputFile.close();
	return input;
}


const RockPaperScissorsPlay Solution::decryptPlay(char encryptedPlay) const {
	switch(encryptedPlay) {
		case 'A':
		case 'X':
			return RockPaperScissorsPlay::Rock;
		case 'B':
		case 'Y':
			return RockPaperScissorsPlay::Paper;
		case 'C':
		case 'Z':
			return RockPaperScissorsPlay::Scissors;
	}

	return RockPaperScissorsPlay::Invalid;
}


int Solution::part1(const Input input) const {
	int accumulator = 0;

	for(const auto& [opponentPlay, yourPlay] : input) {
		accumulator += calculateScore(opponentPlay, yourPlay);
	}

	return accumulator;
}


int Solution::calculateScore(RockPaperScissorsPlay opponentPlay, RockPaperScissorsPlay yourPlay) const {
	int yourPlayScore{ 0 };
	switch(yourPlay) {
		case RockPaperScissorsPlay::Rock:
			yourPlayScore = 1;
			break;
		case RockPaperScissorsPlay::Paper:
			yourPlayScore = 2;
			break;
		case RockPaperScissorsPlay::Scissors:
			yourPlayScore = 3;
			break;
		default:
			break;
	}

	RoundResult result;
	if((yourPlay == RockPaperScissorsPlay::Rock && opponentPlay == RockPaperScissorsPlay::Scissors) ||
		 (yourPlay == RockPaperScissorsPlay::Scissors && opponentPlay == RockPaperScissorsPlay::Paper) ||
		 (yourPlay == RockPaperScissorsPlay::Paper && opponentPlay == RockPaperScissorsPlay::Rock)) {
		result = RoundResult::Won;
	}
	else if(yourPlay == opponentPlay) {
		result = RoundResult::Draw;
	}
	else {
		result = RoundResult::Lost;
	}

	int roundResultScore{ 0 };
	switch(result) {
		case RoundResult::Won:
			roundResultScore = 6;
			break;
		case RoundResult::Draw:
			roundResultScore = 3;
			break;
		case RoundResult::Lost:
			roundResultScore = 0;
			break;
	}

	return yourPlayScore + roundResultScore;
}


int Solution::part2(const Input input) const {
	return -1;
}
	