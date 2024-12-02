import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day02Solution } from "./day02.ts";


describe("Day02Solution", () => {
	const solution = new Day02Solution();

	const sampleInput = [
		[7, 6, 4, 2, 1], // safe (decreasing)
		[1, 2, 7, 8, 9], // unsafe
		[9, 7, 6, 2, 1], // unsafe
		[1, 3, 2, 4, 5], // unsafe
		[8, 6, 4, 4, 1], // unsafe
		[1, 3, 6, 7, 9] // safe (increasing)
	];

	const realInput = solution.parseInput(Deno.readTextFileSync('src/day02/input.txt'));


	describe("parseInput()", () => {

		it("should return the correct value for the sample input", () => {
			const sampleInput = (
				"7 6 4 2 1\n" +
				"1 2 7 8 9\n" +
				"9 7 6 2 1\n" +
				"1 3 2 4 5\n" +
				"8 6 4 4 1\n" +
				"1 3 6 7 9\n"
			);

			expect(solution.parseInput(sampleInput)).toEqual([
				[7, 6, 4, 2, 1],
				[1, 2, 7, 8, 9],
				[9, 7, 6, 2, 1],
				[1, 3, 2, 4, 5],
				[8, 6, 4, 4, 1],
				[1, 3, 6, 7, 9]
			]);
		});

	});


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(solution.part1(sampleInput)).toBe(2);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part1(realInput)).toBe(332);
		});

	});


});
