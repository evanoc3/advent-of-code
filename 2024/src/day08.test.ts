import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect/expect";
import { Day08Solution } from "./day08.ts";


describe("Day08Solution", () => {

	const solution = new Day08Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day08.txt")
	);

	const sampleInput = solution.parseInput(
		"............\n" +
		"........0...\n" +
		".....0......\n" +
		".......0....\n" +
		"....0.......\n" +
		"......A.....\n" +
		"............\n" +
		"............\n" +
		"........A...\n" +
		".........A..\n" +
		"............\n" +
		"............\n"
	);


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part1(sampleInput)
			).toEqual(14);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part1(realInput)
			).toEqual(367);
		});

	});


	describe("part2()", () => {
		
		it("should return the correct value for the sample input", () => {
			expect(
				solution.part2(sampleInput)
			).toEqual(34);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part2(realInput)
			).toEqual(1285);
		});

	});

});
