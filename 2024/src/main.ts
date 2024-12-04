import { Day01Solution } from "./day01.ts";
import { Day02Solution } from "./day02.ts";
import { Day03Solution } from "./day03.ts";


function main(): void {
	const solutions = [
		new Day01Solution(),
		new Day02Solution(),
		new Day03Solution()
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
