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

		const std::pair<const char, const char> pair(line.at(0), line.at(2));
		input.push_back(pair);
	}
	
	inputFile.close();
	return input;
}


const RockPaperScissorsPlay Solution::Part1::decryptPlay(char encryptedPlay) {
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

const int Solution::part1(const Input input) const {
	int accumulator = 0;

	for(const auto& plays : input) {
		const auto opponentPlay = Part1::decryptPlay(plays.first);
		const auto yourPlay = Part1::decryptPlay(plays.second);

		accumulator += Part1::calculateScore(opponentPlay, yourPlay);
	}

	return accumulator;
}

const int Solution::Part1::calculateScore(const RockPaperScissorsPlay opponentPlay, const RockPaperScissorsPlay yourPlay) {
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


const std::pair<const RockPaperScissorsPlay, const RoundResult> Solution::Part2::decryptPlays(std::pair<const char, const char> plays) {
	RockPaperScissorsPlay opponentPlay;
	switch(plays.first) {
		case 'A':
			opponentPlay = RockPaperScissorsPlay::Rock;
			break;
		case 'B':
			opponentPlay = RockPaperScissorsPlay::Paper;
			break;
		case 'C':
			opponentPlay = RockPaperScissorsPlay::Scissors;
			break;
		default:
			break;
	}

	RoundResult desiredResult;
	switch(plays.second) {
		case 'X':
			desiredResult = RoundResult::Lost;
			break;
		case 'Y':
			desiredResult = RoundResult::Draw;
			break;
		case 'Z':
			desiredResult = RoundResult::Won;
			break;
		default:
			break;
	}

	return { opponentPlay, desiredResult };
}

const int Solution::part2(const Input input) const {
	int accumulator = 0;

	for(const auto& plays : input) {
		const auto [opponentPlay, desiredResult] = Part2::decryptPlays(plays);
		accumulator += Part2::calculateScore(opponentPlay, desiredResult);
	}

	return accumulator;
}

int Solution::Part2::calculateScore(RockPaperScissorsPlay opponentPlay, RoundResult desiredResult) {
	const RockPaperScissorsPlay yourPlay = getPlayToAchieveDesiredResult(opponentPlay, desiredResult);

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

	int roundResultScore{ 0 };
	switch(desiredResult) {
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

const RockPaperScissorsPlay Solution::Part2::getPlayToAchieveDesiredResult(const RockPaperScissorsPlay opponentPlay, const RoundResult desiredResult) {
	switch(desiredResult) {
		case RoundResult::Won:
			return getPlayToWinAgainst(opponentPlay);
		case RoundResult::Draw:
			return getPlayToDrawAgainst(opponentPlay);
		case RoundResult::Lost:
			return getPlayToLoseAgainst(opponentPlay);
	}
}

const RockPaperScissorsPlay Solution::Part2::getPlayToWinAgainst(const RockPaperScissorsPlay opponentPlay) {
	switch(opponentPlay) {
		case RockPaperScissorsPlay::Rock:
			return RockPaperScissorsPlay::Paper;
		case RockPaperScissorsPlay::Paper:
			return RockPaperScissorsPlay::Scissors;
		case RockPaperScissorsPlay::Scissors:
			return RockPaperScissorsPlay::Rock;
		default:
			return RockPaperScissorsPlay::Invalid;
	}
}

const RockPaperScissorsPlay Solution::Part2::getPlayToDrawAgainst(const RockPaperScissorsPlay opponentPlay) {
	return opponentPlay;
}

const RockPaperScissorsPlay Solution::Part2::getPlayToLoseAgainst(const RockPaperScissorsPlay opponentPlay) {
	switch(opponentPlay) {
		case RockPaperScissorsPlay::Rock:
			return RockPaperScissorsPlay::Scissors;
		case RockPaperScissorsPlay::Paper:
			return RockPaperScissorsPlay::Rock;
		case RockPaperScissorsPlay::Scissors:
			return RockPaperScissorsPlay::Paper;
		default:
			return RockPaperScissorsPlay::Invalid;
	}
}
	