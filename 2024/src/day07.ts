import type { ISolution } from "./common.ts";


interface CalibrationEquation {
	target: number
	values: number[]
}


export class Day07Solution implements ISolution<CalibrationEquation[], number, any> {

  public parseInput(text: string): CalibrationEquation[] {
		const lines = text.trim().split("\n");

		const eqns: CalibrationEquation[] = [];

		for(const line of lines) {
			const [target, values] = line.split(": ");
			const eqn = {
				target: parseInt(target),
				values: values.trim().split(" ").map(v => parseInt(v, 10))
			};
			eqns.push(eqn);
		}

		return eqns;
  }

  public part1(input: CalibrationEquation[]): number {
		const ops = {
			"+": (a: number, b: number) => a + b,
			"*": (a: number, b: number) => a * b
		};

		const acc = input.reduce((acc, eqn) => {
			return isEquationPossible(eqn, ops) ? acc + eqn.target : acc;
		}, 0);

		return acc;
  }

  public part2(input: CalibrationEquation[]) {
		const ops = {
			"+": (a: number, b: number) => a + b,
			"*": (a: number, b: number) => a * b,
			"||": (a: number, b: number) => Number(String(a) + String(b)),
		};
		
		const acc = input.reduce((acc, eqn) => {
			return isEquationPossible(eqn, ops) ? acc + eqn.target : acc;
		}, 0);

		return acc;
  }

  public main(): void {
		const input = this.parseInput(Deno.readTextFileSync("src/day07.txt"));

		console.log("Day07");
		console.log("Part 1", this.part1(input));
		console.log("Part 2", this.part2(input));
  }

}


if(import.meta.main) {
	const solution = new Day07Solution();
	solution.main();
}


type Operators = Record<string, (a: number, b: number) => number>;


function isEquationPossible(eqn: CalibrationEquation, operators: Operators): boolean {
	if(eqn.values.length === 1) {
		return eqn.values[0] === eqn.target;
	}

	for(const operator of Object.keys(operators)) {
		const newEqn = structuredClone(eqn);
		const operands = newEqn.values.splice(0, 2) as [number, number];
		const newVal = operators[operator](...operands);
		newEqn.values = [newVal, ...newEqn.values];
		if(isEquationPossible(newEqn, operators)) {
			return true;
		}
	}

	return false;
}
