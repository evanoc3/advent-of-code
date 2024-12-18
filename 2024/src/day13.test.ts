import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect/expect";
import { Day13Solution } from "./day13.ts";


describe("Day13Solution", () => {

	const solution = new Day13Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day13.txt")
	);

	const sampleInput = solution.parseInput(
		"Button A: X+94, Y+34\n" +
		"Button B: X+22, Y+67\n" +
		"Prize: X=8400, Y=5400\n" +
		"\n" +
		"Button A: X+26, Y+66\n" +
		"Button B: X+67, Y+21\n" +
		"Prize: X=12748, Y=12176\n" +
		"\n" +
		"Button A: X+17, Y+86\n" +
		"Button B: X+84, Y+37\n" +
		"Prize: X=7870, Y=6450\n" +
		"\n" +
		"Button A: X+69, Y+23\n" +
		"Button B: X+27, Y+71\n" +
		"Prize: X=18641, Y=10279\n"
	);


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part1(sampleInput)
			).toEqual(480);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part1(realInput)
			).toEqual(26_299);
		});

	});


	describe("part2()", () => {

		it("should return the correct value for the real input", () => {
			expect(
				solution.part2(realInput)
			).toEqual(107824497933339);
		});

	});

});
