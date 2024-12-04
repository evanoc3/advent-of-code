import { ISolution } from "./common.ts";


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
			return acc + Number(isReportSafe(report));
		}, 0);
	}

	public part2(reports: number[][]): number {
		return reports.reduce((acc, report) => {
			return acc + Number(isReportSafeWithProblemDampener(report));
		}, 0);
	}

	public main(): void {
		const input = Deno.readTextFileSync("./src/day02.txt");
		const numbers = this.parseInput(input);
		console.log("Day 02");
		console.log("Part 1:", this.part1(numbers));
		console.log("Part 2:", this.part2(numbers));
	}

}


if (import.meta.main) {
	const solution = new Day02Solution();
	solution.main();
}


function isReportSafe(report: number[]): boolean {
	return findRuleBreak(report) === -1;
}

function isReportSafeWithProblemDampener(report: number[]): boolean {
	const dampenedResults = report.map((_, i) => {
		const dampenedReport = report.filter((_, j) => j !== i);
		return isReportSafe(dampenedReport);
	});

	return dampenedResults.some(result => result);
}


type Direction = "+" | "-";

type DirectionCounts = Record<Direction, number>;

/**
 * +1 is added to the return value if it is a valid index, to account for the fact that the deltas list
 * does not contain the first number of the report.
 * 
 * @returns the first index which breaks the rules in the deltas list.
 * */
function findRuleBreak(report: number[]): number {
	const deltas = report.slice(1).map((reportNum, i) => {
		const delta = reportNum - report[i];

		return [
			(delta > 0) ? "+" : "-",
			Math.abs(delta)
		] as [Direction, number];
	});

	const directionCounts = deltas.reduce((acc, [direction, _]) => {
		return {
			...acc,
			[direction]: acc[direction] + 1
		};
	}, { "+": 0, "-": 0 } as DirectionCounts);

	const dominantDirection = (directionCounts["+"] > directionCounts["-"]) ? "+" : "-";

	let ruleBreakIndex = deltas.findIndex(([direction, magnitude]) => {
		return direction !== dominantDirection || magnitude === 0 || magnitude > 3;
	});

	if(ruleBreakIndex > -1) {
		ruleBreakIndex += 1;
	}

	if(ruleBreakIndex === report.length) {
		ruleBreakIndex = -1;
	}

	return ruleBreakIndex;
} 
