import type { ISolution } from "./shared/ISolution.ts";


export class Day11Solution implements ISolution<number[], number, number> {

  public parseInput(text: string): number[] {
		return text.trim().split(" ").map(c => parseInt(c));
  }

  public part1(input: number[]): number {
		for(let i = 0; i < 25; i++) {
			for(let j=0; j < input.length; j++) {
				const num = input[j];
		
				if(num === 0) {
					input[j] = 1;
					continue;
				}
		
				const strum = String(num);
		
				if(strum.length % 2 === 0) {
					const firstHalf = strum.slice(0, strum.length / 2);
					const secondHalf = strum.slice(strum.length / 2);
					input[j] = parseInt(firstHalf);
					input.splice(++j, 0, parseInt(secondHalf));
					continue;
				}
		
				input[j] = input[j] * 2024;
			}
		}
    return input.length;
  }

  public part2(input: number[]): number {
		let map = input.reduce((map, num) => {
			const strum = String(num);
			map[strum] = (map[strum] ?? 0) + 1;
			return map;
		}, {} as { [key: string]: number });

		for(let i = 0; i < 75; i++) {
			const newMap: { [key: string]: number } = {};

			for(const [strum, count] of Object.entries(map)) {
				const num = parseInt(strum);

				if(num === 0) {
					newMap["1"] = (newMap["1"] ?? 0) + count;
				}
				else if(strum.length % 2 === 0) {
					const firstHalf = strum.slice(0, strum.length / 2);

					const secondHalf = strum.slice(strum.length / 2);
					const secondHalfNum = parseInt(secondHalf);
					const secondHalfStrum = String(secondHalfNum);

					newMap[firstHalf] = (newMap[firstHalf] ?? 0) + count;
					newMap[secondHalfStrum] = (newMap[secondHalfStrum] ?? 0) + count;
				}
				else {
					const newStrum = String(num * 2024);
					newMap[newStrum] = (newMap[newStrum] ?? 0) + count;
				}
			}

			map = newMap;
		}

    return Object.values(map).reduce((acc, num) => acc + num, 0);
  }

  public main(): void {
		const input = this.parseInput(
			Deno.readTextFileSync("./src/day11.txt")
		);
		console.log("Day11");
		console.log("Part 1:", this.part1(structuredClone(input)));
		console.log("Part 2:", this.part2(structuredClone(input)));
  }

}

if(import.meta.main) {
	new Day11Solution().main();
}



