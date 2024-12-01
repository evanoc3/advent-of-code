import { Day01Solution } from "./day01/day01.ts";

if(import.meta.main) {
	const solutions = [
		new Day01Solution()
	];

	for(const solution of solutions) {
		solution.main();
		console.log();
	}
}
