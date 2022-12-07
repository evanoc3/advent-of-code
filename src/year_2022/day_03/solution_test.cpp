#include <catch.hpp>
#include "year_2022/day_03/solution.hpp"


using namespace Year2022::Day03;


TEST_CASE("Year2022::Day03::Solution", "[Year2022][Day03]")
{
	const auto solution = std::make_unique<Solution>();

	SECTION("getInput")
	{
		const auto actualInput = solution->getInput();

		const Rucksack expectedInputFront = {
			{ 'B', 'z', 'R', 'm', 'm', 'z', 'Z', 'H', 'z', 'V', 'B', 'z', 'g', 'V', 'Q', 'm', 'Z' },
			{ 'L', 'P', 't', 'q', 'q', 'f', 'f', 'P', 'q', 'W', 'q', 'J', 'm', 'P', 'L', 'l', 'L' }
		};
		REQUIRE( actualInput.front() == expectedInputFront );

		const Rucksack expectedInputBack = {
			{ 'h', 'f', 'H', 'r', 'p', 'p', 'h', 'H', 'B', 'p', 'p', 'f' },
			{ 'T', 'v', 'm', 'z', 'g', 'M', 'm', 'b', 'L', 'b', 'g', 'f' }
		};
		REQUIRE( actualInput.back() == expectedInputBack );
	}

	SECTION("part1")
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

			const auto actualResult = solution->part1(sampleInput);
			REQUIRE( actualResult == 157 );
		}

		GIVEN("Real Input")
		{
			const auto actualResult = solution->part1( solution->getInput() );
			REQUIRE( actualResult == 7824 );
		}
	}

	SECTION("part2")
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

			const auto actualResult = solution->part2(sampleInput);
			REQUIRE( actualResult == 70 );
		}

		GIVEN("Real input")
		{
			const auto actualResult = solution->part2(solution->getInput());
			REQUIRE( actualResult == 2798 );
		}
	}

}
