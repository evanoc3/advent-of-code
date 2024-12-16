import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect/expect";
import { Day07Solution } from "./day07.ts";


describe("Day07Solution", () => {

	const solution = new Day07Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day07.txt")
	);

	const sampleInput = solution.parseInput(
		"190: 10 19\n" +
		"3267: 81 40 27\n" +
		"83: 17 5\n" +
		"156: 15 6\n" +
		"7290: 6 8 6 15\n" +
		"161011: 16 10 13\n" +
		"192: 17 8 14\n" +
		"21037: 9 7 18 13\n" +
		"292: 11 6 16 20\n"
	);


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part1(sampleInput)
			).toEqual(3749);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part1(realInput)
			).toEqual(3_119_088_655_389);
		});

	});


	describe("part2()", () => {
		
		it("should return the correct value for the sample input", () => {
			expect(
				solution.part2(sampleInput)
			).toEqual(11_387);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part2(realInput)
			).toEqual(264_184_041_398_847);
		});

	});

});
