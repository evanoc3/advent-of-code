#pragma once

#include <vector>
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


	class Solution final : public IParseInputConst<const Input>
											 , public ISolutionWithInput<const Input&, const std::string, const std::string> {
	public:
		Solution();
		~Solution() = default;

		// IParseInputConst
		const Input parseInput(const std::string& rawInput) const override;

		// ISolution
		const std::string part1(const Input& input) const override;
		const std::string part2(const Input& input) const override;
		
		// Public Methods
		class Part1 {
		public:
			static void performMove(State& prevState, const MoveInstruction instruction);
		};

		class Part2 {
		public:
			static void performMove(State& prevState, const MoveInstruction instruction);
		};

		const std::string getTopOfStateColumns(const State& state) const;
		const std::string stateToString(const State& state) const; // for debugging only
		const std::string moveInstructionToString(const MoveInstruction& instr) const; // for debugging only

		// Member Variables
		const std::filesystem::path mInputFilePath;
	};

}
