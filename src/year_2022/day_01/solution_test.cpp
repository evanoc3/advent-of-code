#include <catch.hpp>
#include "solution.hpp"
#include "utils/FileUtils.hpp"


using namespace Year2022::Day01;


namespace Year2022::Day01 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("1000\n"
												"2000\n"
												"3000\n"
												"\n"
												"4000\n"
												"\n"
												"5000\n"
												"6000\n"
												"\n"
												"7000\n"
												"8000\n"
												"9000\n"
												"\n"
												"10000\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}

		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day01::Solution::parseInput", "[Year2022][Day01][parseInput]")
{
	GIVEN("Sample input")
	{
		const auto actualParsedInput = mSolution->parseInput(mSampleRawInput);

		const std::vector<std::vector<int>> expectedParsedInput = {
			{ 1000, 2000, 3000 },
			{ 4000 },
			{ 5000, 6000 },
			{ 7000, 8000, 9000 },
			{ 10000 }
		};

		REQUIRE( actualParsedInput == expectedParsedInput );
	}

	GIVEN("Real input")
	{
		const auto actualRawInput = Utils::getFileContents(mSolution->mInputFilePath);
		const auto actualParsedInput = mSolution->parseInput(actualRawInput);

		REQUIRE( actualParsedInput.front() == std::vector<int>{ 3120, 4127, 1830, 1283, 5021, 3569, 3164, 2396, 4367, 2821, 6118, 4450, 1300, 3648, 1933 } );
		REQUIRE( actualParsedInput.back() == std::vector<int>{ 3531, 4133, 1549, 9146, 8227, 5186, 5159, 1952 } );
	}

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day01::Solution::part1", "[Year2022][Day01][part1]")
{
	GIVEN("Sample input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		const auto actualOutput = mSolution->part1(parsedInput);

		REQUIRE( actualOutput == 24000 );
	}

	GIVEN("Real input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		const auto actualResult = mSolution->part1(parsedInput);

		REQUIRE( actualResult == 68292 );
	}
}
	

TEST_CASE_METHOD(SolutionTests, "Year2022::Day01::Solution::part2", "[Year2022][Day01][part2]")
{
	GIVEN("Sample input")
	{
		const auto parsedInput = mSolution->parseInput(mSampleRawInput);
		const auto actualResult = mSolution->part2(parsedInput);

		REQUIRE( actualResult == 45000 );
	}

	GIVEN("Real input")
	{
		const auto parsedInput = mSolution->parseInput(mActualRawInput);
		const auto actualResult = mSolution->part2(parsedInput);

		REQUIRE( actualResult == 203203 );
	}
}

