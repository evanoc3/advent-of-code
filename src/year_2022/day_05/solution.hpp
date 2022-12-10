#pragma once

#include <vector>
#include <string>
#include <deque>
#include "utils/ISolution.hpp"


namespace Year2022::Day05 {

	struct MoveInstruction {
		int amount;
		int srcColumn;
		int destColumn;

		bool operator==(const MoveInstruction& rhs) const;
	};

	using State = std::vector<std::deque<char>>;

	struct Input {
		State initialState;
		std::vector<MoveInstruction> moveInstructions;
	};


	class Solution final : public IGetInput<Input>
											 , public IPart1<Input, std::string> {
	public:
		~Solution() = default;

		const Input getInput() const override;
		const std::string part1(const Input input) const override;

		void performMove(State& prevState, const MoveInstruction instruction) const;
		const std::string getTopOfStateColumns(const State& state) const;
		
	private:
		const std::string stateToString(const State& state) const; // for debugging only
		const std::string moveInstructionToString(const MoveInstruction& instr) const; // for debugging only
	};

}
