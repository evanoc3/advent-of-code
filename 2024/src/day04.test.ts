import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day04Solution } from "./day04.ts";


describe("Day04Solution", () => {
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


	describe("part2()", () => {
		const sampleInput = solution.parseInput(
			".M.S......\n" +
			"..A..MSMS.\n" +
			".M.S.MAA..\n" +
			"..A.ASMSM.\n" +
			".M.S.M....\n" +
			"..........\n" +
			"S.S.S.S.S.\n" +
			".A.A.A.A..\n" +
			"M.M.M.M.M.\n" +
			"..........\n"
		);

		it("should return the correct value for the sample input", () => {
			expect(solution.part2(sampleInput)).toEqual(9);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part2(realInput)).toEqual(1967);
		});

	});

});

