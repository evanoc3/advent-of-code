#pragma once

#include "utils/ISolution.hpp"


namespace Year2022::Day06 {

	using Input = std::string;


	class Solution final : public IGetInput<Input>
											 , public IPart1<Input, int> {
	public:
		~Solution() = default;

		const Input getInput() const override;
		const int part1(const Input input) const override;

		const bool substringIsUnique(const std::string substr) const;

	private:
	};

}
