import {
	Day01Solution,
	Day02Solution
} from "./index.ts";


if(import.meta.main) {
	const solutions = [
		new Day01Solution(),
		new Day02Solution()
	];

	for(const solution of solutions) {
		solution.main();
		console.log();
	}
}
