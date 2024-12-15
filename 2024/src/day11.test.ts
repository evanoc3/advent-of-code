import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day11Solution } from "./day11.ts";


describe("Day11Solution", () => {

	const solution = new Day11Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day11.txt")
	);

	const sampleInput = solution.parseInput(
		"125 17\n"
	);


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part1(structuredClone(sampleInput))
			).toEqual(55_312);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part1(structuredClone(realInput))
			).toEqual(220_999);
		});

	});


	describe("part2()", () => {

		it("should return the correct value for the real input", () => {
			expect(
				solution.part2(structuredClone(realInput))
			).toEqual(261_936_432_123_724);
		});

	});

});
