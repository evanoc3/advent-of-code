import type { ISolution } from "./shared/ISolution.ts";


interface Input {
	rules: [number, number][]
	updates: number[][]
}


export class Day05Solution implements ISolution<Input, number, number> {

  public parseInput(text: string): Input {
		const [ rulesString, updatesString ] = text.trim().split("\n\n"); 

		const rules = [];
		const rulesRegex = /^(\d+)\|(\d+)$/gm;
		let match = rulesRegex.exec(rulesString);
		while(match !== null) {
			rules.push([parseInt(match[1]), parseInt(match[2])] as [number, number]);
			match = rulesRegex.exec(rulesString);
		};

		const updatesLines = updatesString.split("\n");
		const updates = [];
		for(const updateLine of updatesLines) {
			const updatePageStrings = updateLine.trim().split(",");
			updates.push(
				updatePageStrings.map(updatePageString => parseInt(updatePageString, 10))
			);
		}

		return {
			rules,
			updates
		};
  }

  public part1(input: Input): number {
		let acc = 0;

		for(const update of input.updates) {
			const relevantRules = input.rules.filter(([firstPage, lastPage]) => update.includes(firstPage) && update.includes(lastPage));

			if(updateSatisfiesRules(update, relevantRules)) {
				acc += getMiddlePageOfUpdate(update);
			}
		}

		return acc;
  }

  public part2(input: Input): number {
		let acc = 0;

		for(const update of input.updates) {
			const relevantRules = getRelevantRules(update, input.rules);

			const brokenRules = findBrokenRules(update, relevantRules);
			if(brokenRules.length) {
				const fixedUpdate = fixUpdate(update, relevantRules);
				acc += getMiddlePageOfUpdate(fixedUpdate);
			}
		}

		return acc;
  }

  public main(): void {
		const input = this.parseInput(Deno.readTextFileSync("./src/day05.txt"));
		console.log("Day 05");
		console.log("Part 1:", this.part1(input));
		console.log("Part 2:", this.part2(input));
  }

}

if(import.meta.main) {
	new Day05Solution().main();
}


function updateSatisfiesRules(update: number[], rules: [number, number][]): boolean {
	return rules.every(([firstPage, lastPage]) => {
		const firstIndex = update.indexOf(firstPage);
		const lastIndex = update.indexOf(lastPage);
		return firstIndex > -1 && lastIndex > -1 && firstIndex < lastIndex;
	});
}

function getMiddlePageOfUpdate(update: number[]): number {
	return update[Math.floor(update.length / 2)];
}


function findBrokenRules(update: number[], rules: [number, number][]): [number, number][] {
	return rules.filter(([firstPage, lastPage]) => {
		const firstIndex = update.indexOf(firstPage);
		const lastIndex = update.indexOf(lastPage);
		return firstIndex > -1 && lastIndex > -1 && firstIndex > lastIndex;
	});
}


function fixUpdate(update: number[], allRules: [number, number][]): number[] {
	let fixedUpdate: number[] = [];

	for(const updateNum of update) {
		for(let i = 0; i <= fixedUpdate.length; i++) {
			const newFixedUpdate = [...fixedUpdate];
			newFixedUpdate.splice(i, 0, updateNum);

			const relevantRules = getRelevantRules(newFixedUpdate, allRules);
			if(updateSatisfiesRules(newFixedUpdate, relevantRules)) {
				fixedUpdate = newFixedUpdate;
				break;
			}
		}
	}

	return fixedUpdate;
}


function getRelevantRules(update: number[], allRules: [number, number][]): [number, number][] {
	return allRules.filter(([firstPage, lastPage]) => update.includes(firstPage) && update.includes(lastPage));
}
