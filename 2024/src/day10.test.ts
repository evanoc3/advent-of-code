import { describe, it } from "@std/testing/bdd";
import { expect } from "@std/expect";
import { Day10Solution } from "./day10.ts";


describe("Day10Solution", () => {

	const solution = new Day10Solution();

	const realInput = solution.parseInput(
		Deno.readTextFileSync("./src/day10.txt")
	);

	describe("part1()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part1(
					solution.parseInput(
						"89010123\n" +
						"78121874\n" +
						"87430965\n" +
						"96549874\n" +
						"45678903\n" +
						"32019012\n" +
						"01329801\n" +
						"10456732\n"
					)
				)
			).toEqual(36);

			expect(
				solution.part1(
					solution.parseInput(
						"10..9..\n" +
						"2...8..\n" +
						"3...7..\n" +
						"4567654\n" +
						"...8..3\n" +
						"...9..2\n" +
						".....01\n"
					)
				)
			).toEqual(3);

			expect(
				solution.part1(
					solution.parseInput(
						"..90..9\n" +
						"...1.98\n" +
						"...2..7\n" +
						"6543456\n" +
						"765.987\n" +
						"876....\n" +
						"987....\n"
					)
				)
			).toEqual(4);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part1(realInput)
			).toEqual(566);
		});

	});


	describe("part2()", () => {

		it("should return the correct value for the sample input", () => {
			expect(
				solution.part2(
					solution.parseInput(
						".....0.\n" +
						"..4321.\n" +
						"..5..2.\n" +
						"..6543.\n" +
						"..7..4.\n" +
						"..8765.\n" +
						"..9....\n"
					)
				)
			).toEqual(3);

			expect(
				solution.part2(
					solution.parseInput(
						"89010123\n" +
						"78121874\n" +
						"87430965\n" +
						"96549874\n" +
						"45678903\n" +
						"32019012\n" +
						"01329801\n" +
						"10456732\n"
					)
				)
			).toEqual(81);
		});

		it("should return the correct value for the real input", () => {
			expect(
				solution.part2(realInput)
			).toEqual(1324);
		});

	});

});
