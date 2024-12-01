import { ISolution } from "../common.ts";

export class Day01Solution implements ISolution<string[], number, number> {

	public parseInput(text: string): string[] {
		return text.split('\n');
	}

	public part1(input: string[]): number {
		const lists = getSortedLists(input);

		let acc = 0;

		for(let i = 0; i < lists.list1.length; i++) {
			const num1 = lists.list1[i];
			const num2 = lists.list2[i];

			const diff = Math.abs(num1 - num2);
			acc += diff;
		}

		return acc;
	}

	public part2(input: string[]): number {
		const lists = getSortedLists(input);
		return getSimilarityScore(lists.list1, lists.list2);
	}

	public main(): void {
		const inputText = Deno.readTextFileSync('src/day01/input.txt');
		const input = this.parseInput(inputText);

		console.log("Day 01");
		console.log(`Part 1: ${this.part1(input)}`);
		console.log(`Part 2: ${this.part2(input)}`);
	}

}

if (import.meta.main) {
	const solution = new Day01Solution();
	solution.main();
}

function getSortedLists(lines: string[]): { list1: number[], list2: number[] } {
	const input = {
		list1: [],
		list2: []
	};

	for(const line of lines) {
		if(!line) {
			continue;
		}

		const parsedLine = /(\d+)\s+(\d+)/.exec(line);
		if(!parsedLine) {
			throw new Error(`invalid line: "${line}"`);
		}

		const num1 = parseInt(parsedLine[1], 10);
		insertNumIntoList(input.list1, num1);

		const num2 = parseInt(parsedLine[2], 10);
		insertNumIntoList(input.list2, num2);
	}

	return input;
}

function insertNumIntoList(list: number[], num: number): void {
	const index = list.findIndex(n => n > num);
	if(index === -1) {
		list.push(num);
	} else {
		list.splice(index, 0, num);
	}
}

function getSimilarityScore(list1: number[], list2: number[]): number {
	let acc = 0;

	for(const num1 of list1) {
		let occurences = 0;

		for(const num2 of list2) {
			if(num2 < num1) {
				continue;
			}
			if(num2 > num1) {
				break;
			}
			occurences += 1;
		}

		acc += num1 * occurences;
	}

	return acc;
}
