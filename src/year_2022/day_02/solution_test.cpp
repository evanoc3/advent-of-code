#include <catch.hpp>
#include "utils/FileUtils.hpp"
#include "solution.hpp"


using namespace Year2022::Day02;


namespace Year2022::Day02 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("A Y\n"
												"B X\n"
												"C Z\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}
	
		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day02::Solution::parseInput", "[Year2022][Day02][parseInput]")
{
	GIVEN("Sample raw input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);

		REQUIRE( parsedInput.size() == 3 );
		REQUIRE( parsedInput.front().first == 'A' );
		REQUIRE( parsedInput.front().second == 'Y' );

		REQUIRE( parsedInput.back().first == 'C' );
		REQUIRE( parsedInput.back().second == 'Z' );
	}

	GIVEN("Actual raw input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);

		REQUIRE( parsedInput.front().first == 'B' );
		REQUIRE( parsedInput.front().second == 'X' );

		REQUIRE( parsedInput.back().first == 'A' );
		REQUIRE( parsedInput.back().second == 'Y' );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day02::Solution::part1", "[Year2022][Day02][part1]")
{
	GIVEN("Sample input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part1(parsedInput) == 15 );
	}

	GIVEN("Real input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part1(parsedInput) == 15337 );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day02::Solution::part2", "[Year2022][Day02][part2]")
{
	GIVEN("Sample input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part2(parsedInput) == 12 );
	}

	GIVEN("Real input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part2(parsedInput) == 11696 );
	}
}
