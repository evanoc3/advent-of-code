#include <catch.hpp>
#include "solution.hpp"
#include "utils/FileUtils.hpp"


using namespace Year2022::Day08;


namespace Year2022::Day08 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}
		
		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day08::Solution::parseInput", "[Year2022][Day08][parseInput]")
{
	GIVEN("Sample Raw Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		
		// do some assertions on the input
		// REQUIRE( parseInput );
	}
	
	GIVEN("Actual Raw Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		
		// do some assertions on the input
		// REQUIRE( parseInput );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day08::Solution::part1", "[Year2022][Day08][part1]")
{
	GIVEN("Sample Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		
		// do some assertions on the output of part1
		// REQUIRE( mSolution->part1(parsedInput) );
	}
	
	GIVEN("Actual Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		
		// do some assertions on the output of part1
		// REQUIRE( mSolution->part1(parsedInput) );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day08::Solution::part2", "[Year2022][Day08][part2]")
{
	GIVEN("Sample Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		
		// do some assertions on the output of part2
		// REQUIRE( mSolution->part2(parsedInput) );
	}
	
	GIVEN("Actual input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		
		// do some assertions on the output of part2
		// REQUIRE( mSolution->part2(parsedInput) );
	}
}
