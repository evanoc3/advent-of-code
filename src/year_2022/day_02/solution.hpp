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

	using Input = std::vector<std::pair<const RockPaperScissorsPlay, const RockPaperScissorsPlay>>;

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
	
	private:
		const RockPaperScissorsPlay decryptPlay(char encryptedPlay) const;
		int calculateScore(RockPaperScissorsPlay opponentPlay, RockPaperScissorsPlay yourPlay) const;
	};

}