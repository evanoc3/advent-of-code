import type { ISolution } from "./common.ts";


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


interface Position {
	x: number
	y: number
}


class CharMatrix implements Iterable<{ char: string } & Position> {

	private data: string[][];
	private width: number;
	private height: number;

	constructor(data: string) {
		this.data = data.trim().split("\n").map(line => line.split(""));
		this.width = this.data[0].length;
		this.height = this.data.length;
	}

	public charAt(pos: Position): string | undefined {
		if(!this.isInBounds(pos)) {
			return undefined;
		}

		return this.data[pos.y][pos.x];
	}

	public charAtTranslation(start: Position, translation: keyof typeof translations, n: number): string | undefined {
		const translatedPosition = translations[translation](start, n);
		return this.charAt(translatedPosition);
	}

	public [Symbol.iterator](): Iterator<{ char: string } & Position> {
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

	public isInBounds({ x, y }: Position): boolean {
		return y >= 0 && y < this.height && x >= 0 && x < this.width;
	}

}


const translations = {
	"top-left": (pos: Position, n: number) => ({ x: pos.x - n, y: pos.y - n }),
	"top": (pos: Position, n: number) => ({ x: pos.x, y: pos.y - n }),
	"top-right": (pos: Position, n: number) => ({ x: pos.x + n, y: pos.y - n }),
	"right": (pos: Position, n: number) => ({ x: pos.x + n, y: pos.y }),
	"bottom-right": (pos: Position, n: number) => ({ x: pos.x + n, y: pos.y + n }),
	"bottom": (pos: Position, n: number) => ({ x: pos.x, y: pos.y + n }),
	"bottom-left": (pos: Position, n: number) => ({ x: pos.x - n, y: pos.y + n }),
	"left": (pos: Position, n: number) => ({ x: pos.x - n, y: pos.y })
};


function countSearchWordsStartingAt(matrix: CharMatrix, { x, y }: Position): number {
	if(matrix.charAt({ x, y }) !== "X") {
		return 0;
	}

	let count = 0;

	for(const translationDirection of Object.keys(translations)) {
		if(matrix.charAtTranslation({ x, y }, translationDirection as keyof typeof translations, 1) === "M" &&
			matrix.charAtTranslation({ x, y }, translationDirection as keyof typeof translations, 2) === "A" &&
			matrix.charAtTranslation({ x, y }, translationDirection as keyof typeof translations, 3) === "S") {
			count += 1;
		}
	}

	return count;
}

function isXMasCenteredAt(matrix: CharMatrix, { x, y }: Position): boolean {
	if(matrix.charAt({ x, y }) !== "A") {
		return false;
	}

	const topLeft = matrix.charAtTranslation({ x, y }, "top-left", 1);
	const topRight = matrix.charAtTranslation({ x, y }, "top-right", 1);
	const bottomLeft = matrix.charAtTranslation({ x, y }, "bottom-left", 1);
	const bottomRight = matrix.charAtTranslation({ x, y }, "bottom-right", 1);

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


