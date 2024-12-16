import type { ISolution } from "./shared/ISolution.ts";
import { type Coord2D, type Bounds2D, type Vector2D, Direction, directionTranslations, coordIsWithinBounds, coordsAreEqual, vectorsAreEqual } from "./shared/2d.ts";


class Map implements Bounds2D {

	public width!: number;
	public height!: number;
	public guard!: Vector2D;
	public obstacles: Coord2D[] = [];

	public rotateGuardClockwise(): void {
		const newDirectionMapping: Partial<Record<Direction, Direction>> = {
			[Direction.North]: Direction.East,
			[Direction.East]: Direction.South,
			[Direction.South]: Direction.West,
			[Direction.West]: Direction.North
		};

		this.guard.direction = newDirectionMapping[this.guard.direction]!;
	}

	public getPositionsInFrontOf(guard: Vector2D): Coord2D[] {
		const ray: Coord2D[] = [];
		let curPosition = { x: guard.x, y: guard.y };
		while(true) {
			curPosition = directionTranslations[guard.direction](curPosition);

			if(!coordIsWithinBounds(curPosition, this)) {
				break;
			}

			ray.push(curPosition);

			if(this.isObstacleAt(curPosition)) {
				break;
			}
		}

		return ray;
	}

	public isObstacleAt(position: Coord2D): boolean {
		return this.obstacles.some(obstacle => coordsAreEqual(obstacle, position));
	}

	public clone(): Map {
		const newMap = new Map();
		newMap.width = this.width;
		newMap.height = this.height;
		newMap.guard = structuredClone(this.guard);
		newMap.obstacles = structuredClone(this.obstacles);
		return newMap;
	}

}


export class Day06Solution implements ISolution<Map, number, number> {

	public parseInput(text: string): Map {
		const map = new Map();

		const lines = text.trim().split("\n");
		map.width = lines[0].length;
		map.height = lines.length;

		for(let y = 0; y < lines.length; y++) {
			const line = lines[y];
			for(let x = 0; x < line.length; x++) {

				switch(line[x]) {
					case "^":
						map.guard = { x, y, direction: Direction.North };
						break;

					case ">":
						map.guard = { x, y, direction: Direction.East };
						break;

					case "<":
						map.guard = { x, y, direction: Direction.West };
						break;
					
					case "v":
						map.guard = {	x, y, direction: Direction.South };
						break;
					
					case "#":
						map.obstacles.push({ x, y });
						break;

					default:
						break;
				}
			}
		}

		return map;
	}

	public part1(map: Map): number {
		const visitedPositions = [
			structuredClone(map.guard)
		];

		while(true) {
			const forwardLine = map.getPositionsInFrontOf(map.guard);
			if (forwardLine.length === 0) {
				break;
			}

			const isLineEndedAtObstacle = map.isObstacleAt(forwardLine.at(-1)!);
			if(isLineEndedAtObstacle) {
				forwardLine.splice(-1, 1);
			}

			addUniquePositions(visitedPositions, forwardLine);
			
			if(forwardLine.length) {
				map.guard = { ...forwardLine.at(-1)!, direction: map.guard.direction };
			}

			if(isLineEndedAtObstacle)	{
				map.rotateGuardClockwise();
			}
		}

		return visitedPositions.length;
  }

  public part2(map: Map): number {
		let acc = 0;

		for(let y = 0; y < map.height; y++) {
			for(let x = 0; x < map.width; x++) {
				const newMap = map.clone();

				const newObstaclePosition = { x, y };

				if(newMap.isObstacleAt(newObstaclePosition) || coordsAreEqual(newMap.guard, newObstaclePosition)) {
					continue;
				}

				newMap.obstacles.push(newObstaclePosition);

				if(doesGuardPathLoop(newMap)) {
					acc += 1;
				}
			}
		}

		return acc;
  }

  public main(): void {
		const input = this.parseInput(Deno.readTextFileSync("./src/day06.txt"));
		console.log("Day 06");
		console.log("Part 1:", this.part1(input.clone()));
		console.log("Part 2:", this.part2(input.clone()));
  }

}


if(import.meta.main) {
	new Day06Solution().main();
}


function addUniquePositions(positions: Coord2D[], newPositions: Coord2D[]): void {
	for(const newPos of newPositions) {
		if(!positions.some(pos => pos.x === newPos.x && pos.y === newPos.y)) {
			positions.push(newPos);
		}
	}
}


function doesGuardPathLoop(map: Map): boolean {
	const visitedPositions: Vector2D[] = [
		structuredClone(map.guard)
	];

	while(true) {
		const forwardLine = map.getPositionsInFrontOf(map.guard);
		
		if(!forwardLine.length) {
			return false;
		}

		const isLineEndedAtObstacle = map.isObstacleAt(forwardLine.at(-1)!);
		if(isLineEndedAtObstacle) {
			forwardLine.splice(-1, 1);
		}

		for(const newPos of forwardLine) {
			const visited: Vector2D = {
				...newPos, direction: map.guard.direction
			};
			if(visitedPositions.some(pos => vectorsAreEqual(pos, visited))) {
				return true;
			}

			visitedPositions.push(visited);
		}
		
		if(forwardLine.length) {
			map.guard = { ...forwardLine.at(-1)!, direction: map.guard.direction };
		}

		if(isLineEndedAtObstacle)	{
			map.rotateGuardClockwise();

			if(visitedPositions.some(pos => vectorsAreEqual(pos, map.guard))) {
				return true;
			}
			else {
				visitedPositions.push(structuredClone(map.guard));
			}
		}
	}
}
