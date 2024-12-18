import type { ISolution } from "./shared/ISolution.ts";
import type { Coord2D } from "./shared/2d.ts";


const A_BUTTON_COST = 3;
const B_BUTTON_COST = 1;
const ERROR_FACTOR = 10_000_000_000_000;
const FLOAT_ERR_THRESHOLD = 0.0001;


interface ClawMachine {
	a: Coord2D
	b: Coord2D
	p: Coord2D
}


export class Day13Solution implements ISolution<ClawMachine[], number, number> {

  public parseInput(text: string): ClawMachine[]{
		const machines: ClawMachine[] = [];

		for(const machineText of text.trim().split("\n\n")) {
			const aMoveMatch = machineText.match(/A: X\+(\d+), Y\+(\d+)/);
			const bMoveMatch = machineText.match(/B: X\+(\d+), Y\+(\d+)/);
			const prizeMatch = machineText.match(/X=(\d+), Y=(\d+)/);

			if(!aMoveMatch || !bMoveMatch || !prizeMatch) {
				continue;
			}

			machines.push({
				a: { x: parseInt(aMoveMatch[1], 10), y: parseInt(aMoveMatch[2], 10) },
				b: { x: parseInt(bMoveMatch[1], 10), y: parseInt(bMoveMatch[2], 10) },
				p: { x: parseInt(prizeMatch[1], 10), y: parseInt(prizeMatch[2], 10) }
			});
		}

		return machines;
  }

  public part1(machines: ClawMachine[]): number {
		let acc = 0;

		for(const m of machines) {
			let aPresses = ((m.p.x * m.b.y) - (m.p.y * m.b.x)) / ((m.a.x * m.b.y) - (m.a.y * m.b.x));
			let bPresses = ((m.a.x * m.p.y) - (m.a.y * m.p.x)) / ((m.a.x * m.b.y) - (m.a.y * m.b.x));

			if(
				Math.abs(aPresses - Math.round(aPresses)) < 0.0001 ||
				Math.abs(bPresses - Math.round(bPresses)) < 0.0001
			) {
				aPresses = Math.round(aPresses);
				bPresses = Math.round(bPresses);
			} else {
				continue;
			}

			acc += aPresses * A_BUTTON_COST + bPresses * B_BUTTON_COST;
		}

		return acc;
  }

  public part2(machines: ClawMachine[]): number {
		let acc = 0;

		for(const m of machines) {
			const px = m.p.x + ERROR_FACTOR;
			const py = m.p.y + ERROR_FACTOR;

			let aPresses = ((px * m.b.y) - (py * m.b.x)) / ((m.a.x * m.b.y) - (m.a.y * m.b.x));
			let bPresses = ((m.a.x * py) - (m.a.y * px)) / ((m.a.x * m.b.y) - (m.a.y * m.b.x));

			const aPressesImprecision = Math.abs(aPresses - Math.round(aPresses));
			const bPressesImprecision = Math.abs(bPresses - Math.round(bPresses));

			if(aPressesImprecision > FLOAT_ERR_THRESHOLD || bPressesImprecision > FLOAT_ERR_THRESHOLD) {
				continue;
			}

			if(aPressesImprecision > 0 && aPressesImprecision < 0.0001) {
				aPresses = Math.round(aPresses);
			}

			if(bPressesImprecision > 0 && bPressesImprecision < 0.0001) {
				bPresses = Math.round(bPresses);
			}

			acc += aPresses * A_BUTTON_COST + bPresses * B_BUTTON_COST;
		}

		return acc;
  }

  public main(): void {
		const input = this.parseInput(
			Deno.readTextFileSync("./src/day13.txt")
		);
		console.log("Day13");
		console.log("Part 1:", this.part1(input));
		console.log("Part 2:", this.part2(input));
  }

}

if(import.meta.main) {
	new Day13Solution().main();
}
