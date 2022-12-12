#pragma once


/* Get Input Templates */

template<typename Input_t>
class IGetInputMutable {
public:
	virtual Input_t getInput() = 0;
};

template<typename Input_t>
class IGetInput {
public:
	virtual Input_t getInput() const = 0;
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
