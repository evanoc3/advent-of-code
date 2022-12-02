#pragma once

template<typename Input_t, typename Part1_t, typename Part2_t>
class BaseSolution {
public:
	virtual Input_t getInput() const = 0;
	virtual Part1_t part1(const Input_t input) const = 0;
	virtual Part2_t part2(const Input_t input) const = 0;
};
