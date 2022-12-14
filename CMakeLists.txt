cmake_minimum_required(VERSION 3.25)

project(AdventOfCode VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set strict compiler options
if(MSVC)
  add_compile_options(/W4 /WX)
else()
  add_compile_options(-Wall -Werror)
endif()


# Main library
add_library(
	lib-advent-of-code

	src/utils/FileUtils.cpp
	src/year_2022/day_01/solution.cpp
	src/year_2022/day_02/solution.cpp
	src/year_2022/day_03/solution.cpp
	src/year_2022/day_04/solution.cpp
	src/year_2022/day_05/solution.cpp
	src/year_2022/day_06/solution.cpp
	src/year_2022/day_07/solution.cpp
)

target_include_directories(lib-advent-of-code PUBLIC src)


# Main executable
add_executable(
	advent-of-code

	src/main.cpp
)

target_link_libraries(advent-of-code PRIVATE lib-advent-of-code)


# Test executable
add_executable(
	advent-of-code-tests

	src/test_runner.cpp
	src/year_2022/day_01/solution_test.cpp
	src/year_2022/day_02/solution_test.cpp
	src/year_2022/day_03/solution_test.cpp
	src/year_2022/day_04/solution_test.cpp
	src/year_2022/day_05/solution_test.cpp
	src/year_2022/day_06/solution_test.cpp
	src/year_2022/day_07/solution_test.cpp
)

find_package(Catch2 REQUIRED)
target_link_libraries(advent-of-code-tests PRIVATE Catch2::Catch2 lib-advent-of-code)

add_test(NAME advent-of-code-tests COMMAND advent-of-code-tests)
