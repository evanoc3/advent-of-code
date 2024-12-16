import type { ISolution } from "./shared/ISolution.ts";
import { type Bounds2D, type Coord2D, Direction, directionTranslations } from "./shared/2d.ts";
import { coordIsWithinBounds } from "./shared/2d.ts";


export class Day04Solution implements ISolution<CharMatrix, number, number> {

	public parseInput(text: string): CharMatrix {
		return new CharMatrix(text);
	}

	public part1(input: CharMatrix): number {
		let acc = 0;
		for(const { x, y } of input) {
			acc += countSearchWordsStartingAt(input, { x, y });
		}

		return acc;
	}

	public part2(input: CharMatrix): number {
		let acc = 0;
		for(const { x, y } of input) {
			acc += Number(isXMasCenteredAt(input, { x, y }));
		}

		return acc;
	}

	public main(): void {
		const input = this.parseInput(Deno.readTextFileSync("./src/day04.txt"));
		console.log("Day 04");
		console.log("Part 1:", this.part1(input));
		console.log("Part 2:", this.part2(input));
	}

}


if (import.meta.main) {
	const solution = new Day04Solution();
	solution.main();
}


class CharMatrix implements Bounds2D, Iterable<{ char: string } & Coord2D> {

	private data: string[][];
	readonly width: number;
	readonly height: number;

	constructor(data: string) {
		this.data = data.trim().split("\n").map(line => line.split(""));
		this.width = this.data[0].length;
		this.height = this.data.length;
	}

	public charAt(pos: Coord2D): string | undefined {
		if(!coordIsWithinBounds(pos, this)) {
			return undefined;
		}

		return this.data[pos.y][pos.x];
	}

	public charAtTranslation(start: Coord2D, translationDirection: Direction, n: number): string | undefined {
		const translatedPosition = directionTranslations[translationDirection](start, n);
		return this.charAt(translatedPosition);
	}

	public [Symbol.iterator](): Iterator<{ char: string } & Coord2D> {
		const maxX = this.width * this.height;
		let i = 0;
		return {
			next: () => {
				const x = i % this.width;
				const y = Math.floor(i / this.width);
				i++;
				return {
					value: { char: this.charAt({ x, y })!, x, y },
					done: i > maxX
				};
			}
		};
	}

}


function countSearchWordsStartingAt(matrix: CharMatrix, { x, y }: Coord2D): number {
	if(matrix.charAt({ x, y }) !== "X") {
		return 0;
	}

	let count = 0;

	for(const translationDirection of Object.values(Direction)) {
		if(matrix.charAtTranslation({ x, y }, translationDirection, 1) === "M" &&
			matrix.charAtTranslation({ x, y }, translationDirection, 2) === "A" &&
			matrix.charAtTranslation({ x, y }, translationDirection, 3) === "S") {
			count += 1;
		}
	}

	return count;
}

function isXMasCenteredAt(matrix: CharMatrix, { x, y }: Coord2D): boolean {
	if(matrix.charAt({ x, y }) !== "A") {
		return false;
	}

	const topLeft = matrix.charAtTranslation({ x, y }, Direction.NorthWest, 1);
	const topRight = matrix.charAtTranslation({ x, y }, Direction.NorthEast, 1);
	const bottomLeft = matrix.charAtTranslation({ x, y }, Direction.SouthWest, 1);
	const bottomRight = matrix.charAtTranslation({ x, y }, Direction.SouthEast, 1);

	if(!topLeft || !topRight || !bottomLeft || !bottomRight) {
		return false;
	}

	const charCounts = [topLeft, topRight, bottomLeft, bottomRight].reduce((counts, char) => {
		return {
			...counts,
			[char]: (counts[char] ?? 0) + 1
		};
	}, {} as Record<string, number>);

	if(charCounts["M"] !== 2 || charCounts["S"] !== 2) {
		return false;
	}

	return (
		(topLeft === "M" && topRight === "M") ||
		(topRight === "M" && bottomRight === "M") ||
		(bottomRight === "M" && bottomLeft === "M") ||
		(bottomLeft === "M" && topLeft === "M")
	);
	}


