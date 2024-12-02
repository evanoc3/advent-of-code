import { ISolution } from "../common.ts";


export class Day02Solution implements ISolution<number[][], number, number> {

	public parseInput(text: string): number[][] {
		const lines = text.trim().split('\n');
		const numbers = lines.map(line => {
			return line.split(' ').map(num => parseInt(num, 10));
		});
		return numbers;
	}

	public part1(reports: number[][]): number {
		return reports.reduce((acc, report) => {
			return acc + (isReportSafe(report) ? 1 : 0);
		}, 0);
	}

	public part2(_numbers: number[][]): number {
		return 0;
	}

	public main(): void {
		const input = Deno.readTextFileSync('src/day02/input.txt');
		const numbers = this.parseInput(input);
		console.log("Day 02");
		console.log('Part 1:', this.part1(numbers));
		console.log('Part 2:', this.part2(numbers));
	}

}


if (import.meta.main) {
	const solution = new Day02Solution();
	solution.main();
}


function isReportSafe(report: number[]): boolean {
	const direction = (report[0] > report.at(-1)!) ? "decreasing" : "increasing";
	for(let i = 0; i < report.length; i++) {
		if(i === 0) {
			continue;
		}

		const prev = report[i - 1];
		const cur = report[i];

		const newDirection = (prev > cur) ? "decreasing" : "increasing";
		if(newDirection !== direction) {
			return false;
		}

		const delta = Math.abs(prev - cur);
		if (delta === 0 || delta > 3) {
			return false;
		}
	}
	return true;
}
