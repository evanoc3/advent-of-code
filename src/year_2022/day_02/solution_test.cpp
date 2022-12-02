#include <catch.hpp>
#include "year_2022/day_02/solution.hpp"


using namespace Year2022::Day02;


TEST_CASE("Year2022::Day02::Solution", "[Year2022][Day02]")
{
	const auto solution = std::make_unique<Solution>();

	SECTION("getInput")
	{
		const auto actualInput = solution->getInput();
		REQUIRE( actualInput.front().first == RockPaperScissorsPlay::Paper );
		REQUIRE( actualInput.front().second == RockPaperScissorsPlay::Rock );

		REQUIRE( actualInput.back().first == RockPaperScissorsPlay::Rock );
		REQUIRE( actualInput.back().second == RockPaperScissorsPlay::Paper );
	}

	SECTION("part1")
	{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{ RockPaperScissorsPlay::Rock, RockPaperScissorsPlay::Paper },
				{ RockPaperScissorsPlay::Paper, RockPaperScissorsPlay::Rock },
				{ RockPaperScissorsPlay::Scissors, RockPaperScissorsPlay::Scissors }
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
}
