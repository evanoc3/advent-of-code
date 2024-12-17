import type { ISolution } from "./shared/ISolution.ts";
import { type Coord2D, coordsAreAdjacent, coordsAreEqual, Direction, directionTranslations } from "./shared/2d.ts";


interface Region {
	plotType: string
	positions: Coord2D[] 
}


export class Day12Solution implements ISolution<Region[], number, number> {

  public parseInput(text: string): Region[] {
		const plots: ({ plotType: string } & Coord2D)[] = [];

		const lines = text.trim().split("\n");
		for(let y = 0; y < lines.length; y++) {
			for(let x = 0; x < lines[y].length; x++) {
				plots.push({ x, y, plotType: lines[y][x] });
			}
		}

		const regions: Region[] = [];

		while(plots.length > 0) {
			const firstPlot = plots.shift()!;
			const newRegion = {
				plotType: firstPlot.plotType,
				positions: [ firstPlot ]
			}

			let foundAdjacent = true;
			while(foundAdjacent) {
				foundAdjacent = false;

				for(let i = 0; i < plots.length; i++) {
					const plot = plots[i];

					if(plot.plotType !== newRegion.plotType) {
						continue;
					}

					foundAdjacent = newRegion.positions.some(regPos => coordsAreAdjacent(regPos, plot));

					if(foundAdjacent) {
						newRegion.positions.push(plot);
						plots.splice(i, 1);
						break;
					}
				}
			}

			regions.push(newRegion);
		}

		return regions;
  }

  public part1(regions: Region[]): number {
		return regions.reduce((acc, region) => {
			const regionArea = region.positions.length;
			const regionPerimeter = calculateRegionPerimeter(region);
			return acc + (regionArea * regionPerimeter);
		}, 0);
  }

  public part2(regions: Region[]): number {
		return regions.reduce((acc, region) => {
			const regionArea = region.positions.length;
			const regionSides = calculateRegionSides(region);
			return acc + (regionArea * regionSides);
		}, 0);
  }

  public main(): void {
		const input = this.parseInput(
			Deno.readTextFileSync("src/day12.txt")
		);
		console.log("Day12");
		console.log("Part 1:", this.part1(input));
		console.log("Part 2:", this.part2(input));
  }

}

if(import.meta.main) {
	new Day12Solution().main();
}


function calculateRegionPerimeter(region: Region): number {
	return region.positions.reduce((acc, pos) => {
		const adjacentPositions = [
			{ x: pos.x - 1, y: pos.y },
			{ x: pos.x + 1, y: pos.y },
			{ x: pos.x, y: pos.y - 1 },
			{ x: pos.x, y: pos.y + 1 }
		];
		const adjacentPositionsInRegion = adjacentPositions.filter(adjPos => (
			region.positions.some(regionPos => coordsAreEqual(regionPos, adjPos)))
		);
		return acc + (4 - adjacentPositionsInRegion.length);
	}, 0);
}

function calculateRegionSides(region: Region): number {
	return region.positions.reduce((acc, pos) => {
		return acc + calculateRegionPositionCorners(pos, region.positions);
	}, 0);
}


function calculateRegionPositionCorners(pos: Coord2D, region: Coord2D[]): number {
	const exposedSides: Direction[] = [];
	const unexposedSides: Direction[] = [];

	for(const direction of Object.values(Direction)) {
		const translatedPos = directionTranslations[direction](pos);
		const isUnexposed = region.some(regionPos => coordsAreEqual(regionPos, translatedPos));
		if(isUnexposed) {
			unexposedSides.push(direction);
		} else {
			exposedSides.push(direction);
		}
	}

	let corners = 0;

	// north-west
	if(
		(exposedSides.includes(Direction.North) && exposedSides.includes(Direction.West)) ||
		(unexposedSides.includes(Direction.North) && unexposedSides.includes(Direction.West) && exposedSides.includes(Direction.NorthWest))
	) {
		corners += 1;
	}

	// north-east
	if(
		(exposedSides.includes(Direction.North) && exposedSides.includes(Direction.East)) ||
		(unexposedSides.includes(Direction.North) && unexposedSides.includes(Direction.East) && exposedSides.includes(Direction.NorthEast))
	) {
		corners += 1;
	}

	// south-east
	if(
		(exposedSides.includes(Direction.South) && exposedSides.includes(Direction.East)) ||
		(unexposedSides.includes(Direction.South) && unexposedSides.includes(Direction.East) && exposedSides.includes(Direction.SouthEast))
	) {
		corners += 1;
	}

	// south-west
	if(
		(exposedSides.includes(Direction.South) && exposedSides.includes(Direction.West)) ||
		(unexposedSides.includes(Direction.South) && unexposedSides.includes(Direction.West) && exposedSides.includes(Direction.SouthWest))
	) {
		corners += 1;
	}

	return corners;
}
