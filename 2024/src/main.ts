import { Day01Solution } from "./day01.ts";
import { Day02Solution } from "./day02.ts";
import { Day03Solution } from "./day03.ts";
import { Day04Solution } from "./day04.ts";
import { Day05Solution } from "./day05.ts";
import { Day06Solution } from "./day06.ts";


function main(): void {
	const solutions = [
		new Day01Solution(),
		new Day02Solution(),
		new Day03Solution(),
		new Day04Solution(),
		new Day05Solution(),
		new Day06Solution()
	];

	solutions.forEach((solution, i) => {
		solution.main();

		if(i < solutions.length - 1) {
			console.log();
		}
	});
}


if(import.meta.main) {
	main();
}
