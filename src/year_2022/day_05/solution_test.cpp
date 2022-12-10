#include <catch.hpp>
#include "solution.hpp"


using namespace Year2022::Day05;


namespace Year2022::Day05 {

	class SolutionTests {
	public:
		SolutionTests()	
			: solution(std::make_unique<Solution>()) {
		}

		std::unique_ptr<Solution> solution;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::getInput", "[Year2022][Day05]")
{
	const auto actualInput = solution->getInput();

	// test initialState
	REQUIRE( actualInput.initialState.size() == 9 );
	REQUIRE(actualInput.initialState[0] == std::deque<char>{'S', 'P', 'H', 'V', 'F', 'G'});
	REQUIRE(actualInput.initialState[8] == std::deque<char>{'J', 'Q', 'V', 'P', 'G', 'L', 'F'});

	// test moveInstructions
	REQUIRE(actualInput.moveInstructions.size() ==  502);
	REQUIRE(actualInput.moveInstructions.front() == MoveInstruction{ 6, 9, 3 });
	REQUIRE(actualInput.moveInstructions.back() == MoveInstruction{ 1, 5, 9 });
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


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::part1", "[Year2022][Day05]")
{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{
					{ 'N', 'Z' },
					{ 'D', 'C', 'M' },
					{ 'P' }
				},
				{
					{ 1, 2, 1 },
					{ 3, 1, 3 },
					{ 2, 2, 1 },
					{ 1, 1, 2 }
				}
			};

			REQUIRE( solution->part1(sampleInput) == "CMZ" );
		}

		GIVEN("Real input")
		{
			REQUIRE( solution->part1(solution->getInput()) == "FCVRLMVQP" );
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


TEST_CASE_METHOD(SolutionTests, "Year2022::Day05::Solution::part2", "[Year2022][Day05]")
{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{
					{ 'N', 'Z' },
					{ 'D', 'C', 'M' },
					{ 'P' }
				},
				{
					{ 1, 2, 1 },
					{ 3, 1, 3 },
					{ 2, 2, 1 },
					{ 1, 1, 2 }
				}
			};

			REQUIRE( solution->part2(sampleInput) == "MCD" );
		}

		GIVEN("Real input")
		{
			REQUIRE( solution->part2(solution->getInput()) == "RWLWGJGFD" );
		}
}
