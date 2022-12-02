#pragma once

#include <vector>
#include <string>
#include <utility>
#include "utils/base_solution.hpp"


namespace Year2022::Day02 {

	enum class RockPaperScissorsPlay {
		Invalid,
		Rock,
		Paper,
		Scissors
	};

	using Input = std::vector<std::pair<const char, const char>>;

	enum class RoundResult {
		Won,
		Lost,
		Draw
	};


	class Solution final : public BaseSolution<const Input, int, int> {
	public:
		~Solution() = default;

		const Input getInput() const override;
		int part1(const Input input) const override;
		int part2(const Input input) const override;

		class Part1 {
		public:
			static int calculateScore(RockPaperScissorsPlay opponentPlay, RockPaperScissorsPlay yourPlay);
			static const RockPaperScissorsPlay decryptPlay(char encryptedPlay);
		};

		class Part2 {
		public:
			static int calculateScore(RockPaperScissorsPlay opponentPlay, RoundResult desiredResult);
			static const std::pair<const RockPaperScissorsPlay, const RoundResult> decryptPlays(std::pair<const char, const char> plays);
			static const RockPaperScissorsPlay getPlayToAchieveDesiredResult(const RockPaperScissorsPlay opponentPlay, const RoundResult desiredResult);
			static const RockPaperScissorsPlay getPlayToWinAgainst(const RockPaperScissorsPlay opponentPlay);
			static const RockPaperScissorsPlay getPlayToDrawAgainst(const RockPaperScissorsPlay opponentPlay);
			static const RockPaperScissorsPlay getPlayToLoseAgainst(const RockPaperScissorsPlay opponentPlay);
		};
	};

}