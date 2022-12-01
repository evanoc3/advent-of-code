#include <catch.hpp>
#include "year_2022/day_01/solution.hpp"


using namespace Year2022::Day01;


TEST_CASE("Year2022::Day01::Solution", "[Year2022][Day01]")
{
	const auto solution = Solution();

	SECTION("part1")
	{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{ 1000, 2000, 3000 },
				{ 4000 },
				{ 5000, 6000 },
				{ 7000, 8000, 9000 },
				{ 10000 }
			};

			const auto actualResult = solution.part1(sampleInput);

			const auto expectedResult = 24000;

			REQUIRE( actualResult == expectedResult );
		}

		GIVEN("Real input")
		{
			const auto input = solution.getInput();
			const auto actualResult = solution.part1(input);

			const auto expectedResult = 68292;

			REQUIRE( actualResult == expectedResult );
		}
	}

	SECTION("part2")
	{
		GIVEN("Sample input")
		{
			const Input sampleInput = {
				{ 1000, 2000, 3000 },
				{ 4000 },
				{ 5000, 6000 },
				{ 7000, 8000, 9000 },
				{ 10000 }
			};

			const auto actualResult = solution.part2(sampleInput);

			const auto expectedResult = 45000;

			REQUIRE( actualResult == expectedResult );
		}

		GIVEN("Real input")
		{
			const auto input = solution.getInput();
			const auto actualResult = solution.part2(input);

			const auto expectedResult = 203203;

			REQUIRE( actualResult == expectedResult );
		}
	}
}
