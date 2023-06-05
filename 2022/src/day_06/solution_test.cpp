#include <catch.hpp>
#include "utils/FileUtils.hpp"
#include "solution.hpp"


using namespace Year2022::Day06;


namespace Year2022::Day06 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("mjqjpqmgbljsphdztnvjfqwrcgsmlb\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}
	
		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day06::Solution::part1", "[Year2022][Day06][part1]")
{
	GIVEN("Sample Input")
	{
		REQUIRE( mSolution->part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7 );
		REQUIRE( mSolution->part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5 );
		REQUIRE( mSolution->part1("nppdvjthqldpwncqszvftbrmjlhg") == 6 );
		REQUIRE( mSolution->part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10 );
		REQUIRE( mSolution->part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11 );
	}
	
	GIVEN("Actual Input")
	{
		REQUIRE( mSolution->part1(mActualRawInput) == 1598 );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day06::Solution::part2", "[Year2022][Day06][part2]")
{
	GIVEN("Sample input")
	{
		REQUIRE( mSolution->part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19 );
		REQUIRE( mSolution->part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23 );
		REQUIRE( mSolution->part2("nppdvjthqldpwncqszvftbrmjlhg") == 23 );
		REQUIRE( mSolution->part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29 );
		REQUIRE( mSolution->part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26 );
	}
	
	GIVEN("Real input")
	{
		REQUIRE( mSolution->part2(mActualRawInput) == 2414 );
	}
}
