#pragma once


template<typename Input_t>
class IGetInput {
public:
	virtual const Input_t getInput() const = 0;
};


template<typename Input_t, typename Part1_t>
class IPart1 {
public:
	virtual const Part1_t part1(const Input_t input) const = 0;
};


template<typename Input_t, typename Part2_t>
class IPart2 {
public:
	virtual const Part2_t part2(const Input_t input) const = 0;
};


template<typename Input_t, typename Part1_t, typename Part2_t>
class ISolution : public IGetInput<Input_t>
								, public IPart1<Input_t, Part1_t>
								, public IPart2<Input_t, Part2_t> {
};
