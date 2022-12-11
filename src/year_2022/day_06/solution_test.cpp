#include <catch.hpp>
#include "solution.hpp"


using namespace Year2022::Day06;


namespace Year2022::Day06 {

	class SolutionTests {
	public:
		SolutionTests()
			: solution(std::make_unique<Solution>()) {
		}
		
		std::unique_ptr<Solution> solution;
	};

}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day06::Solution::getInput", "[Year2022][Day06]")
{
	const auto actualInput = solution->getInput();

	REQUIRE( actualInput.at(0) == 'q' );
	REQUIRE( actualInput.at(1) == 'f' );

	REQUIRE( actualInput.at(actualInput.size() - 1) == 'f' );
	REQUIRE( actualInput.at(actualInput.size() - 2) == 't' );
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day06::Solution::part1", "[Year2022][Day06]")
{
	GIVEN("Sample input")
	{
		REQUIRE( solution->part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7 );
		REQUIRE( solution->part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5 );
		REQUIRE( solution->part1("nppdvjthqldpwncqszvftbrmjlhg") == 6 );
		REQUIRE( solution->part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10 );
		REQUIRE( solution->part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11 );
	}
	
	GIVEN("Real input")
	{
		// do some assertions on the output of part1 here
		// const auto expectedOutput = /* insert the expected output here */;
		// REQUIRE( solution->part1(solution->getInput()) == expectedOutput );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day06::Solution::part2", "[Year2022][Day06]")
{
	GIVEN("Sample input")
	{
		const Input sampleInput = {
			/* insert the sample input from the problem here */
		};
		
		// do some assertions on the output of part2 here
		// const auto expectedOutput = /* insert the expected output here */;
		// REQUIRE( solution->part1(sampleInput) == expectedOutput );
	}
	
	GIVEN("Real input")
	{
		// do some assertions on the output of part2 here
		// const auto expectedOutput = /* insert the expected output here */;
		// REQUIRE( solution->part2(solution->getInput()) == expectedOutput );
	}
}
