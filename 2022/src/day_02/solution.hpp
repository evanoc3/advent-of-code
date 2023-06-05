#pragma once

#include <vector>
#include <utility>
#include "utils/ISolution.hpp"


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


	class Solution final : public IParseInputConst<const Input>
											 , public ISolutionWithInput<const Input&, const int, const int> {
	public:
		Solution();
		~Solution() = default;

		// IParseInputConst
		const Input parseInput(const std::string& rawInput) const override;

		// ISolutionWithInput
		const int part1(const Input& input) const override;
		const int part2(const Input& input) const override;

		// Public Members
		class Part1 {
		public:
			static const int calculateScore(const RockPaperScissorsPlay opponentPlay, const RockPaperScissorsPlay yourPlay);
			static const RockPaperScissorsPlay decryptPlay(const char encryptedPlay);
		};

		class Part2 {
		public:
			static int calculateScore(RockPaperScissorsPlay opponentPlay, RoundResult desiredResult);
			static const std::pair<const RockPaperScissorsPlay, const RoundResult> decryptPlays(const std::pair<const char, const char> plays);
			static const RockPaperScissorsPlay getPlayToAchieveDesiredResult(const RockPaperScissorsPlay opponentPlay, const RoundResult desiredResult);
			static const RockPaperScissorsPlay getPlayToWinAgainst(const RockPaperScissorsPlay opponentPlay);
			static const RockPaperScissorsPlay getPlayToDrawAgainst(const RockPaperScissorsPlay opponentPlay);
			static const RockPaperScissorsPlay getPlayToLoseAgainst(const RockPaperScissorsPlay opponentPlay);
		};

		// Member Variables
		const std::filesystem::path mInputFilePath;
	};

}
