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
	src/day_01/solution.cpp
	src/day_02/solution.cpp
	src/day_03/solution.cpp
	src/day_04/solution.cpp
	src/day_05/solution.cpp
	src/day_06/solution.cpp
	src/day_07/solution.cpp
	src/day_08/solution.cpp
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
	src/day_01/solution_test.cpp
	src/day_02/solution_test.cpp
	src/day_03/solution_test.cpp
	src/day_04/solution_test.cpp
	src/day_05/solution_test.cpp
	src/day_06/solution_test.cpp
	src/day_07/solution_test.cpp
	src/day_08/solution_test.cpp
)

find_package(Catch2 REQUIRED)
target_link_libraries(advent-of-code-tests PRIVATE Catch2::Catch2 lib-advent-of-code)

add_test(NAME advent-of-code-tests COMMAND advent-of-code-tests)
