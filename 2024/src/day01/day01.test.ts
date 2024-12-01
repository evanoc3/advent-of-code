import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day01Solution } from "./day01.ts";


describe("Day01Solution", () => {
	const solution = new Day01Solution();

	const sampleInput = [
		"3   4\n",
		"4   3\n",
		"2   5\n",
		"1   3\n",
		"3   9\n",
		"3   3\n",
	];

	const realInput = solution.parseInput(Deno.readTextFileSync("src/day01/input.txt"));

	describe("part1()", () => {

		it("should return the correect value for the sample input", () => {
			expect(solution.part1(sampleInput)).toBe(11);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part1(realInput)).toBe(2285373);
		});

	});

	describe("part2()", () => {
		
		it("should return the correct value for the sample input", () => {
			expect(solution.part2(sampleInput)).toBe(31);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part2(realInput)).toBe(21142653);
		});

	});

});
