#include <catch.hpp>
#include "utils/FileUtils.hpp"
#include "solution.hpp"


using namespace Year2022::Day05;


namespace Year2022::Day05 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("    [D]    \n"
												"[N] [C]    \n"
												"[Z] [M] [P]\n"
												" 1   2   3 \n"
												"\n"
												"move 1 from 2 to 1\n"
												"move 3 from 1 to 3\n"
												"move 2 from 2 to 1\n"
												"move 1 from 1 to 2\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}
	
		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::parseInput", "[Year2022][Day05][parseInput]")
{
	GIVEN("Sample Raw Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
	}

	GIVEN("Actual Raw Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);

		// test initialState
		REQUIRE( parsedInput.initialState.size() == 9 );
		REQUIRE( parsedInput.initialState[0] == std::deque<char>{'S', 'P', 'H', 'V', 'F', 'G'} );
		REQUIRE( parsedInput.initialState[8] == std::deque<char>{'J', 'Q', 'V', 'P', 'G', 'L', 'F'} );

		// test moveInstructions
		REQUIRE( parsedInput.moveInstructions.size() ==  502 );
		REQUIRE( parsedInput.moveInstructions.front() == MoveInstruction{ 6, 9, 3 } );
		REQUIRE( parsedInput.moveInstructions.back() == MoveInstruction{ 1, 5, 9 } );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::Part1::performMove", "[Year2022][Day05]")
{
	State actualState = {
		{ 'N', 'Z' },
		{ 'D', 'C', 'M' },
		{ 'P' }
	};

	// test first move instruction
	Solution::Part1::performMove(actualState, { 1, 2, 1 });
	State expectedState = {
		{ 'D', 'N', 'Z' },
		{ 'C', 'M' },
		{ 'P' }
	};
	REQUIRE(actualState == expectedState);

	// test second move instruction
	Solution::Part1::performMove(actualState, { 3, 1, 3 });
	expectedState = {
		{ },
		{ 'C', 'M' },
		{ 'Z', 'N', 'D', 'P' }
	};
	REQUIRE(actualState == expectedState);

	// test third move instruction
	Solution::Part1::performMove(actualState, { 2, 2, 1 });
	expectedState = {
		{ 'M', 'C' },
		{ },
		{ 'Z', 'N', 'D', 'P' }
	};
	REQUIRE(actualState == expectedState);

	// fourth move instruction
	Solution::Part1::performMove(actualState, { 1, 1, 2 });
	expectedState = {
		{ 'C' },
		{ 'M' },
		{ 'Z', 'N', 'D', 'P' }
	};
	REQUIRE(actualState == expectedState);
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::part1", "[Year2022][Day05][part1]")
{
	GIVEN("Sample Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part1(parsedInput) == "CMZ" );
	}

	GIVEN("Actual Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part1(parsedInput) == "FCVRLMVQP" );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::Part2::performMove", "[Year2022][Day05]")
{
	State actualState = {
		{ 'N', 'Z' },
		{ 'D', 'C', 'M' },
		{ 'P' }
	};

	// test first move instruction
	Solution::Part2::performMove(actualState, { 1, 2, 1 });
	State expectedState = {
		{ 'D', 'N', 'Z' },
		{ 'C', 'M' },
		{ 'P' }
	};
	REQUIRE(actualState == expectedState);

	// test second move instruction
	Solution::Part2::performMove(actualState, { 3, 1, 3 });
	expectedState = {
		{ },
		{ 'C', 'M' },
		{ 'D', 'N', 'Z', 'P' }
	};
	REQUIRE(actualState == expectedState);

	// test third move instruction
	Solution::Part2::performMove(actualState, { 2, 2, 1 });
	expectedState = {
		{ 'C', 'M' },
		{ },
		{ 'D', 'N', 'Z', 'P' }
	};
	REQUIRE(actualState == expectedState);

	// fourth move instruction
	Solution::Part2::performMove(actualState, { 1, 1, 2 });
	expectedState = {
		{ 'M' },
		{ 'C' },
		{ 'D', 'N', 'Z', 'P' }
	};
	REQUIRE(actualState == expectedState);
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::part2", "[Year2022][Day05][part2]")
{
	GIVEN("Sample Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part2(parsedInput) == "MCD" );
	}

	GIVEN("Actual Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part2(parsedInput) == "RWLWGJGFD" );
	}
}
