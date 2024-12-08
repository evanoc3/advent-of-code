import type { ISolution } from "./common.ts";


class Map {

	public width!: number;
	public height!: number;
	public guard!: PositionAndDirection;
	public obstacles: Position[] = [];

	public rotateGuardClockwise(): void {
		const newDirectionMapping: Record<Direction, Direction> = {
			[Direction.North]: Direction.East,
			[Direction.East]: Direction.South,
			[Direction.South]: Direction.West,
			[Direction.West]: Direction.North
		};

		this.guard.direction = newDirectionMapping[this.guard.direction];
	}

	public getPositionsInFrontOf(guard: PositionAndDirection): Position[] {
		const translations: Record<Direction, (p: Position) => Position> = {
			[Direction.North]: ({ x, y }) => ({ x, y: y - 1 }),
			[Direction.South]: ({ x, y }) => ({ x, y: y + 1 }),
			[Direction.East]: ({ x, y }) => ({ x: x + 1, y }),
			[Direction.West]: ({ x, y }) => ({ x: x - 1, y })
		};

		const ray: Position[] = [];
		let curPosition = { x: guard.x, y: guard.y };
		while(true) {
			curPosition = translations[guard.direction](curPosition);

			if(curPosition.x < 0 || curPosition.x >= this.width || curPosition.y < 0 || curPosition.y >= this.height) {
				break;
			}

			ray.push(curPosition);

			if(this.isObstacleAt(curPosition)) {
				break;
			}
		}

		return ray;
	}

	public isObstacleAt(position: Position): boolean {
		return this.obstacles.some(obstacle => obstacle.x === position.x && obstacle.y === position.y);
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

				if(newMap.isObstacleAt(newObstaclePosition) || isPositionsEqual(newMap.guard, newObstaclePosition)) {
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


interface Position {
	x: number;
	y: number;
}


const enum Direction {
	North = "n",
	East = "e",
	South = "s",
	West = "w"
}


interface PositionAndDirection extends Position {
	direction: Direction;
};


function addUniquePositions(positions: Position[], newPositions: Position[]): void {
	for(const newPos of newPositions) {
		if(!positions.some(pos => pos.x === newPos.x && pos.y === newPos.y)) {
			positions.push(newPos);
		}
	}
}


function isPositionsEqual(posA: Position, posB: Position): boolean {
	return posA.x === posB.x && posA.y === posB.y;
}


function isPositionsAndDirectionsEqual(posA: PositionAndDirection, posB: PositionAndDirection): boolean {
	return isPositionsEqual(posA, posB) && posA.direction === posB.direction;

}


function doesGuardPathLoop(map: Map): boolean {
	const visitedPositions: PositionAndDirection[] = [
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
			const visited: PositionAndDirection = {
				...newPos, direction: map.guard.direction
			};
			if(visitedPositions.some(pos => isPositionsAndDirectionsEqual(pos, visited))) {
				return true;
			}

			visitedPositions.push(visited);
		}
		
		if(forwardLine.length) {
			map.guard = { ...forwardLine.at(-1)!, direction: map.guard.direction };
		}

		if(isLineEndedAtObstacle)	{
			map.rotateGuardClockwise();

			if(visitedPositions.some(pos => isPositionsAndDirectionsEqual(pos, map.guard))) {
				return true;
			} else {
				visitedPositions.push(structuredClone(map.guard));
			}
		}
	}
}
