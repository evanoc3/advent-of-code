#include <catch.hpp>
#include "utils/FileUtils.hpp"
#include "solution.hpp"


using namespace Year2022::Day03;


namespace Year2022::Day03 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("vJrwpWtwJgWrhcsFMMfFFhFp\n"
												"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n"
												"PmmdzqPrVvPwwTWBwg\n"
												"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n"
												"ttgJtRGJQctTZtZT\n"
												"CrZsJsPPZsGzwwsLwLmpwMDw\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}
	
		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day03::Solution::parseInput", "[Year2022][Day03][parseInput]")
{
	GIVEN("Sample Input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( parsedInput.size() == 6 );

		const Rucksack expectedFront = {
			{ 'v', 'J', 'r', 'w', 'p', 'W', 't', 'w', 'J', 'g', 'W', 'r' },
			{ 'h', 'c', 's', 'F', 'M', 'M', 'f', 'F', 'F', 'h', 'F', 'p' }
		};
		REQUIRE( parsedInput.front() == expectedFront );

		const Rucksack expectedBack = {
			{ 'C', 'r', 'Z', 's', 'J', 's', 'P', 'P', 'Z', 's', 'G', 'z' },
			{ 'w', 'w', 's', 'L', 'w', 'L', 'm', 'p', 'w', 'M', 'D', 'w' }
		};
		REQUIRE( parsedInput.back() == expectedBack );
	}

	GIVEN("Actual Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);

		const Rucksack expectedInputFront = {
			{ 'B', 'z', 'R', 'm', 'm', 'z', 'Z', 'H', 'z', 'V', 'B', 'z', 'g', 'V', 'Q', 'm', 'Z' },
			{ 'L', 'P', 't', 'q', 'q', 'f', 'f', 'P', 'q', 'W', 'q', 'J', 'm', 'P', 'L', 'l', 'L' }
		};
		REQUIRE( parsedInput.front() == expectedInputFront );

		const Rucksack expectedInputBack = {
			{ 'h', 'f', 'H', 'r', 'p', 'p', 'h', 'H', 'B', 'p', 'p', 'f' },
			{ 'T', 'v', 'm', 'z', 'g', 'M', 'm', 'b', 'L', 'b', 'g', 'f' }
		};
		REQUIRE( parsedInput.back() == expectedInputBack );
	}
}

TEST_CASE_METHOD(SolutionTests, "Year2022::Day03::Solution::part1", "[Year2022][Day03][part1]")
{
	GIVEN("Sample input")
	{
		const Input sampleInput = {
			{ { 'v', 'J', 'r', 'w', 'p', 'W', 't', 'w', 'J', 'g', 'W', 'r' }, { 'h', 'c', 's', 'F', 'M', 'M', 'f', 'F', 'F', 'h', 'F', 'p' } },
			{ { 'j', 'q', 'H', 'R', 'N', 'q', 'R', 'j', 'q', 'z', 'j', 'G', 'D', 'L', 'G', 'L' }, { 'r', 's', 'F', 'M', 'f', 'F', 'Z', 'S', 'r', 'L', 'r', 'F', 'Z', 's', 'S', 'L' } },
			{ { 'P', 'm', 'm', 'd', 'z', 'q', 'P', 'r', 'V' }, { 'v', 'P', 'w', 'w', 'T', 'W', 'B', 'w', 'g' } },
			{ { 'w', 'M', 'q', 'v', 'L', 'M', 'Z', 'H', 'h', 'H', 'M', 'v', 'w', 'L', 'H' }, { 'j', 'b', 'v', 'c', 'j', 'n', 'n', 'S', 'B', 'n', 'v', 'T', 'Q', 'F', 'n' } },
			{ { 't', 't', 'g', 'J', 't', 'R', 'G', 'J' }, { 'Q', 'c', 't', 'T', 'Z', 't', 'Z', 'T' } },
			{ { 'C', 'r', 'Z', 's', 'J', 's', 'P', 'P', 'Z', 's', 'G', 'z' }, { 'w', 'w', 's', 'L', 'w', 'L', 'm', 'p', 'w', 'M', 'D', 'w' } }
		};

		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part1(parsedInput) == 157 );
	}

	GIVEN("Real Input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part1(parsedInput) == 7824 );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day03::Solution::part2", "[Year2022][Day03][part2]")
{
	GIVEN("Sample input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		REQUIRE( mSolution->part2(parsedInput) == 70 );
	}

	GIVEN("Actual input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part2(parsedInput) == 2798 );
	}
}


