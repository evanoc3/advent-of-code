#include <catch.hpp>
#include "year_2022/day_02/solution.hpp"


using namespace Year2022::Day02;


TEST_CASE("Year2022::Day02::Solution", "[Year2022][Day02]")
{
	const auto solution = std::make_unique<Solution>();

	SECTION("getInput")
	{
		const auto actualInput = solution->getInput();
		REQUIRE( actualInput.front().first == 'B' );
		REQUIRE( actualInput.front().second == 'X' );

		REQUIRE( actualInput.back().first == 'A' );
		REQUIRE( actualInput.back().second == 'Y' );
	}

	SECTION("part1")
	{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{ 'A', 'Y' },
				{ 'B', 'X' },
				{ 'C', 'Z' }
			};

			const auto actualResult = solution->part1(sampleInput);
			REQUIRE( actualResult == 15 );
		}

		GIVEN("Real input")
		{
			const auto actualResult = solution->part1( solution->getInput() );
			REQUIRE( actualResult == 15337 );
		}
	}

	SECTION("part2")
	{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{ 'A', 'Y' },
				{ 'B', 'X' },
				{ 'C', 'Z' }
			};

			const auto actualResult = solution->part2(sampleInput);
			REQUIRE( actualResult == 12 );
		}

		GIVEN("Real input")
		{
			const auto actualResult = solution->part2(solution->getInput());
			REQUIRE( actualResult == 11696 );
		}
	}


}
