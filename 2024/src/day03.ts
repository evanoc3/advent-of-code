import type { ISolution } from "./shared/ISolution.ts";


export class Day03Solution implements ISolution<string, number, number> {

	public parseInput(text: string): string {
		return text.trim();
	}

	public part1(input: string): number {
		const mulArgs = parseMultiplyInstructions(input);

		let acc = 0;

		for(const [a, b] of mulArgs) {
			acc += a * b;
		}

		return acc;
	}

	public part2(input: string): number {
		const ops = parseMultiplyOpsAndConditionals(input);

		let isAccEnabled = true;
		let acc = 0;
		for(const op of ops) {
			if(typeof op === "boolean") {
				isAccEnabled = op;
				continue;
			}
			else /* if(Array.isArray(op)) */ {
				if(!isAccEnabled) {
					continue;
				}
				const [arg1, arg2] = op;
				acc += arg1 * arg2;
			}
		}

		return acc;
	}

	public main(): void {
		const input = Deno.readTextFileSync("./src/day03.txt");
		const parsedInput = this.parseInput(input);
		console.log("Day 03");
		console.log("Part 1:", this.part1(parsedInput));
		console.log("Part 2:", this.part2(parsedInput));
	}

}

if (import.meta.main) {
	const solution = new Day03Solution();
	solution.main();
}


function parseMultiplyInstructions(input: string): [number, number][] {
	const rgx = /mul\((\d{1,3}),(\d{1,3})\)/gm;

	const mulArgs: [number, number][] = [];

	while(true) {
		const matches = rgx.exec(input);
		if(!matches) {
			break;
		}

		mulArgs.push([parseInt(matches[1], 10), parseInt(matches[2], 10)]);
	}

	return mulArgs;
}


function parseMultiplyOpsAndConditionals(input: string): ([number, number] | boolean)[] {
	const rgx = /(?:mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))/gm;

	const ops: ([number, number] | boolean)[] = [];

	while(true) {
		const matches = rgx.exec(input);
		if(!matches) {
			break;
		}

		if(matches[0].startsWith("mul")) {
			ops.push([parseInt(matches[1], 10), parseInt(matches[2], 10)]);
		} else if(matches[0] === "do()") {
			ops.push(true);
		} else /* if(matches[0] === "don't()") */ {
			ops.push(false);
		}
	}

	return ops;
}
