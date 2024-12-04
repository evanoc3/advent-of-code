import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day03Solution } from "./day03.ts";


describe("Day03Solution", () => {
	const solution = new Day03Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day03.txt")
	);


	describe("part1()", () => {

		const sampleInput = (
			"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
		);

		it("should return the correct value for the sample input", () => {
			expect(solution.part1(sampleInput)).toEqual(161);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part1(realInput)).toEqual(175700056);
		});

	});


	describe("part2()", () => {

		const sampleInput = (
			"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
		);
		
		it("should return the correct value for the sample input", () => {
			expect(solution.part2(sampleInput)).toEqual(48);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part2(realInput)).toEqual(71668682);
		});

	});

});

