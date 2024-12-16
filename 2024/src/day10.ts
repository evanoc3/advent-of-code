import type { ISolution } from "./shared/ISolution.ts";
import type { Coord2D, Matrix2D } from "./shared/2d.ts";


interface Input {
	map: Matrix2D
	trailHeads: Coord2D[]
}


export class Day10Solution implements ISolution<Input, number, number> {
	
  public parseInput(text: string): Input {
		const map = text.trim().split("\n").map(line => line.split("").map(char => parseInt(char, 10)));

		const trailHeads: Coord2D[] = [];
		for(let y = 0; y < map.length; y++) {
			for(let x = 0; x < map[y].length; x++) {
				if(map[y][x] === 0) {
					trailHeads.push({ x, y });
				}
			}
		}

		return {
			trailHeads,
			map
		};
  }

  public part1({ trailHeads, map }: Input): number {
    return trailHeads.reduce((acc, trailHead) => acc + getTrailScore(trailHead, map, []), 0);
  }

  public part2({ trailHeads, map }: Input): number {
		return trailHeads.reduce((acc, trailHead) => acc + getTrailRating(trailHead, map), 0);
  }

  public main(): void {
		const input = this.parseInput(
			Deno.readTextFileSync("./src/day10.txt")
		);
		console.log("Day10");
		console.log("Part 1:", this.part1(input));
		console.log("Part 2:", this.part2(input));
  }

}


if(import.meta.main) {
	new Day10Solution().main();
}


function getTrailScore(curPos: Coord2D, map: Matrix2D, trailPeaks: Coord2D[]): number {
	const curHeight = map[curPos.y][curPos.x];

	if(curHeight === 9) {
		trailPeaks.push(curPos);
		return 1;
	}

	const adjacentPositions = getAdjacentPositions(curPos, map);

	const trailNextStepPositions = adjacentPositions.filter(pos => (
		map[pos.y][pos.x] === curHeight + 1 && !trailPeaks.some(peak => peak.x === pos.x && peak.y === pos.y)
	));

	return trailNextStepPositions.reduce((acc, nextPos) => (
		acc + getTrailScore(nextPos, map, trailPeaks)
	), 0);
}


function getAdjacentPositions(pos: Coord2D, map: Matrix2D): Coord2D[] {
	const positions: Coord2D[] = [];

	if(pos.y > 0) {
		positions.push({ x: pos.x, y: pos.y - 1 });
	}
	if(pos.y < map.length - 1) {
		positions.push({ x: pos.x, y: pos.y + 1 });
	}
	if(pos.x > 0) {
		positions.push({ x: pos.x - 1, y: pos.y });
	}
	if(pos.x < map[0].length - 1) {
		positions.push({ x: pos.x + 1, y: pos.y });
	}

	return positions;
}


function getTrailRating(curPos: Coord2D, map: Matrix2D): number {
	const curHeight = map[curPos.y][curPos.x];

	if(curHeight === 9) {
		return 1;
	}

	const adjacentPositions = getAdjacentPositions(curPos, map);

	const trailNextStepPositions = adjacentPositions.filter(pos => (
		map[pos.y][pos.x] === curHeight + 1
	));

	return trailNextStepPositions.reduce((acc, nextPos) => (
		acc + getTrailRating(nextPos, map)
	), 0);
}
