#include <catch.hpp>
#include "utils/FileUtils.hpp"
#include "solution.hpp"


using namespace Year2022::Day04;


namespace Year2022::Day04 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("2-4,6-8\n"
												"2-3,4-5\n"
												"5-7,7-9\n"
												"2-8,3-7\n"
												"6-6,4-6\n"
												"2-6,4-8\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}
	
		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day04::Solution::parseInput", "[Year2022][Day04][parseInput]")
{
	GIVEN("Sample Raw Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);

		REQUIRE( parsedInput.front().first == range(2, 4) );
		REQUIRE( parsedInput.front().second == range(6, 8) );

		REQUIRE( parsedInput.back().first == range(2, 6) );
		REQUIRE( parsedInput.back().second == range(4, 8) );
	}

	GIVEN("Actual Raw Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);

		REQUIRE( parsedInput.front().first == range(7, 24) );
		REQUIRE( parsedInput.front().second == range(8, 8) );

		REQUIRE( parsedInput.back().first == range(23, 79) );
		REQUIRE( parsedInput.back().second == range(22, 24) );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day04::Solution::part1", "[Year2022][Day04][part1]")
{
	GIVEN("Sample input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part1(parsedInput) == 2 );
	}

	GIVEN("Real input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part1(parsedInput) == 562 );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day04::Solution::part2", "[Year2022][Day04][part2]")
{
	GIVEN("Sample input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part2(parsedInput) == 4 );
	}

	GIVEN("Real input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part2(parsedInput) == 924 );
	}
}

