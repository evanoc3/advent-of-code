import { Day01Solution } from "./day01.ts";
import { Day02Solution } from "./day02.ts";
import { Day03Solution } from "./day03.ts";
import { Day04Solution } from "./day04.ts";
import { Day05Solution } from "./day05.ts";
import { Day06Solution } from "./day06.ts";
import { Day07Solution } from "./day07.ts";
import { Day08Solution } from "./day08.ts";
import { Day09Solution } from "./day09.ts";
import { Day10Solution } from "./day10.ts";
import { Day11Solution } from "./day11.ts";
import { Day12Solution } from "./day12.ts";
import { Day13Solution } from "./day13.ts";


const solutions = [
	new Day01Solution(),
	new Day02Solution(),
	new Day03Solution(),
	new Day04Solution(),
	new Day05Solution(),
	new Day06Solution(),
	new Day07Solution(),
	new Day08Solution(),
	new Day09Solution(),
	new Day10Solution(),
	new Day11Solution(),
	new Day12Solution(),
	new Day13Solution(),
];


function main(): void {
	if(Deno.args.length === 1) {
		const n = parseInt(Deno.args[0]);
		if(isNaN(n)) {
			console.error(`Error: failed to parse argument "${Deno.args[0]}"`);
			Deno.exit(1);
		}
		runSpecificSolution(n);
		return;
	}

	runAllSolutions();
}


if(import.meta.main) {
	main();
}


function runSpecificSolution(n: number): void {
	const i = n - 1;
	solutions[i].main();
}


function runAllSolutions(): void {
	solutions.forEach((solution, i) => {
		solution.main();

		if(i < solutions.length - 1) {
			console.log();
		}
	});
}

