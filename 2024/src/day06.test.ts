import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day06Solution } from "./day06.ts";


describe("Day06Solution", () => {
	const solution = new Day06Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day06.txt")
	);

	const sampleInput = solution.parseInput(
		"....#....#\n" +
		".........#\n" +
		"..........\n" +
		"..#.......\n" +
		".......#..\n" +
		"..........\n" +
		".#..^.....\n" +
		"........#.\n" +
		"#.........\n" +
		"......#...\n"
	);


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(solution.part1(sampleInput.clone())).toEqual(41);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part1(realInput.clone())).toEqual(4819);
		});

	});


	describe("part2()", () => {

		it("should return the correct value for the sample input", () => {
			// expect(solution.part2(sampleInput.clone())).toEqual(6);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part2(realInput.clone())).toEqual(Number.POSITIVE_INFINITY);
		});

	});

});

