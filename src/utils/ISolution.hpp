#pragma once

#include <string>
#include <filesystem>


/* Get Input Templates */

template<typename Input_t>
class IParseInput {
public:
	virtual Input_t parseInput(const std::string& rawInput) = 0;

	const std::filesystem::path mInputFilePath;
};

template<typename Input_t>
class IParseInputConst {
public:
	virtual Input_t parseInput(const std::string& rawInput) const = 0;

	const std::filesystem::path mInputFilePath;
};


/* Part 1 Templates */

template<typename Part1_t>
class IPart1 {
public:
	virtual Part1_t part1() const = 0;
};

template <typename Input_t, typename Part1_t>
class IPart1WithInput {
public:
	virtual Part1_t part1(Input_t input) const = 0;
};


/* Part 2 Templates */

template<typename Part2_t>
class IPart2 {
public:
	virtual Part2_t part2() const = 0;
};

template<typename Input_t, typename Part2_t>
class IPart2WithInput {
public:
	virtual Part2_t part2(Input_t input) const = 0;
};


/* Combination Solution Templates */

template<typename Part1_t, typename Part2_t>
class ISolution : public IPart1<Part1_t>
								, public IPart2<Part2_t> {
};

template<typename Input_t, typename Part1_t, typename Part2_t>
class ISolutionWithInput : public IPart1WithInput<Input_t, Part1_t>
												 , public IPart2WithInput<Input_t, Part2_t> {
};
