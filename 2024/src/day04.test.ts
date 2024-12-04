import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day04Solution } from "./day04.ts";


describe("Day03Solution", () => {
	const solution = new Day04Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day04.txt")
	);


	describe("part1()", () => {

		const sampleInput = solution.parseInput(
			"MMMSXXMASM\n" +
			"MSAMXMSMSA\n" +
			"AMXSXMAAMM\n" +
			"MSAMASMSMX\n" +
			"XMASAMXAMM\n" +
			"XXAMMXXAMA\n" +
			"SMSMSASXSS\n" +
			"SAXAMASAAA\n" +
			"MAMMMXMMMM\n" +
			"MXMXAXMASX\n"
		);

		it("should return the correct value for the sample input", () => {
			expect(solution.part1(sampleInput)).toEqual(18);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part1(realInput)).toEqual(2496);
		});

	});

});

