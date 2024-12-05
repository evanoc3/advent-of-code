import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day05Solution } from "./day05.ts";


describe("Day05Solution", () => {
	const solution = new Day05Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day05.txt")
	);

	const sampleInput = solution.parseInput(
		"47|53\n" +
		"97|13\n" +
		"97|61\n" +
		"97|47\n" +
		"75|29\n" +
		"61|13\n" +
		"75|53\n" +
		"29|13\n" +
		"97|29\n" +
		"53|29\n" +
		"61|53\n" +
		"97|53\n" +
		"61|29\n" +
		"47|13\n" +
		"75|47\n" +
		"97|75\n" +
		"47|61\n" +
		"75|61\n" +
		"47|29\n" +
		"75|13\n" +
		"53|13\n" +
		"\n" +
		"75,47,61,53,29\n" +
		"97,61,53,29,13\n" +
		"75,29,13\n" +
		"75,97,47,61,53\n" +
		"61,13,29\n" +
		"97,13,75,29,47\n"
	);


	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(solution.part1(sampleInput)).toEqual(143);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part1(realInput)).toEqual(6384);
		});

	});


	describe("part2()", () => {

		it("should return the correct value for the sample input", () => {
			expect(solution.part2(sampleInput)).toEqual(123);
		});

		it("should return the correct value for the real input", () => {
			expect(solution.part2(realInput)).toEqual(5353);
		});

	});

});

