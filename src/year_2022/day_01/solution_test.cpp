#include <catch.hpp>
#include "year_2022/day_01/solution.hpp"


using namespace Year2022::Day01;


TEST_CASE("Year2022::Day01::Solution", "[Year2022][Day01]")
{
	const auto solution = std::make_unique<Solution>();

	SECTION("getInput")
	{
		const auto actualInput = solution->getInput();

		const std::vector<int> expectedInputFront = { 3120, 4127, 1830, 1283, 5021, 3569, 3164, 2396, 4367, 2821, 6118, 4450, 1300, 3648, 1933 };

		REQUIRE( actualInput.front() == expectedInputFront );

		const std::vector<int> expectedInputBack = { 3531, 4133, 1549, 9146, 8227, 5186, 5159, 1952 };

		REQUIRE( actualInput.back() == expectedInputBack );
	}

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

			const auto actualResult = solution->part1(sampleInput);

			const auto expectedResult = 24000;

			REQUIRE( actualResult == expectedResult );
		}

		GIVEN("Real input")
		{
			const auto input = solution->getInput();
			const auto actualResult = solution->part1(input);

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

			const auto actualResult = solution->part2(sampleInput);

			const auto expectedResult = 45000;

			REQUIRE( actualResult == expectedResult );
		}

		GIVEN("Real input")
		{
			const auto input = solution->getInput();
			const auto actualResult = solution->part2(input);

			const auto expectedResult = 203203;

			REQUIRE( actualResult == expectedResult );
		}
	}
}
