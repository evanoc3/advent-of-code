#include <catch.hpp>
#include "year_2022/day_04/solution.hpp"


using namespace Year2022::Day04;


TEST_CASE("Year2022::Day04::Solution", "[Year2022][Day04]")
{
	const auto solution = std::make_unique<Solution>();

	SECTION("getInput")
	{
		const auto actualInput = solution->getInput();

		REQUIRE( actualInput.front().first == range(7, 24) );
		REQUIRE( actualInput.front().second == range(8, 8) );

		REQUIRE( actualInput.back().first == range(23, 79) );
		REQUIRE( actualInput.back().second == range(22, 24) );
	}

	SECTION("part1")
	{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{ {2, 4}, {6, 8} },
				{ {2, 3}, {4, 5} },
				{ {5, 7}, {7, 9} },
				{ {2, 8}, {3, 7} },
				{ {6, 6}, {4, 6} },
				{ {2, 6}, {4, 8} }
			};

			REQUIRE( solution->part1(sampleInput) == 2 );
		}

		GIVEN("Real input") {
			REQUIRE( solution->part1(solution->getInput()) == 562 );
		}
	}
}
