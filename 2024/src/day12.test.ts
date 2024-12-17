import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day12Solution } from "./day12.ts";


describe("Day12Solution", () => {

	const solution = new Day12Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day12.txt")
	);

	const sampleInput = solution.parseInput(
		"AAAA\n" +
		"BBCD\n" +
		"BBCC\n" +
		"EEEC\n"
	);

	const sampleInput2 = solution.parseInput(
		"OOOOO\n" +
		"OXOXO\n" +
		"OOOOO\n" +
		"OXOXO\n" +
		"OOOOO\n"
	);

	const sampleInput3 = solution.parseInput(
		"RRRRIICCFF\n" +
		"RRRRIICCCF\n" +
		"VVRRRCCFFF\n" +
		"VVRCCCJFFF\n" +
		"VVVVCJJCFE\n" +
		"VVIVCCJJEE\n" +
		"VVIIICJJEE\n" +
		"MIIIIIJJEE\n" +
		"MIIISIJEEE\n" +
		"MMMISSJEEE\n"
	);

	describe("part1()", () => {

		it("should return the correct value for the sample inputs", () => {
			expect(
				solution.part1(structuredClone(sampleInput))
			).toEqual(140);

			expect(
				solution.part1(structuredClone(sampleInput2))
			).toEqual(772);

			expect(
				solution.part1(structuredClone(sampleInput3))
			).toEqual(1930);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part1(structuredClone(realInput))
			).toEqual(1431440);
		});

	});


	describe("part2()", () => {

		const sampleInput4 = solution.parseInput(
			"EEEEE\n" +
			"EXXXX\n" +
			"EEEEE\n" +
			"EXXXX\n" +
			"EEEEE\n"
		);

		const sampleInput5 = solution.parseInput(
			"AAAAAA\n" +
			"AAABBA\n" +
			"AAABBA\n" +
			"ABBAAA\n" +
			"ABBAAA\n" +
			"AAAAAA\n"
		);

		it("should return the correct value for the sample inputs", () => {
			expect(
				solution.part2(sampleInput)
			).toBe(80);

			expect(
				solution.part2(sampleInput2)
			).toBe(436);

			expect(
				solution.part2(sampleInput4)
			).toBe(236);

			expect(
				solution.part2(sampleInput5)
			).toBe(368);

			expect(
				solution.part2(sampleInput3)
			).toBe(1206);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part2(structuredClone(realInput))
			).toEqual(869070);
		});

	});

});
