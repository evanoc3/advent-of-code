import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day09Solution } from "./day09.ts";


describe("Day09Solution", () => {

	const solution = new Day09Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day09.txt")
	);

	const sampleInput = solution.parseInput(
		"2333133121414131402"
	);


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part1(structuredClone(sampleInput))
			).toEqual(1928);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part1(structuredClone(realInput))
			).toEqual(6353658451014);
		});

	});


	describe("part2()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part2(structuredClone(sampleInput))
			).toEqual(2858);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part2(structuredClone(realInput))
			).toEqual(6382582136592);
		});

	});

});
