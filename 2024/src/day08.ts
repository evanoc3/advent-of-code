import type { ISolution } from "./shared/ISolution.ts";
import type { Coord2D, Bounds2D } from "./shared/2d.ts";


interface Map extends Bounds2D {
	antennae: { [key: string]: Antenna[] }
}


interface Antenna extends Coord2D {
  frequency: string
}


export class Day08Solution implements ISolution<Map, number, number> {

  public parseInput(text: string): Map {
    const lines = text.trim().split("\n");

    const map: Map = {
      width: lines[0].length,
      height: lines.length,
      antennae: {
        all: []
      }
    };

    lines.forEach((line, y) => {
      line.split("").forEach((char, x) => {
        if (char !== ".") {
          const antenna = { x, y, frequency: char };

          map.antennae.all.push(antenna);

          if(char in map.antennae) {
            map.antennae[char].push(antenna);
          } else {
            map.antennae[char] = [antenna];
          }
        }
      });
    });

    return map;
  }

  public part1(map: Map): number {
    let acc = 0;

    for(let y = 0; y < map.height; y++) {
      for(let x = 0; x < map.width; x++) {
        acc += Number(isPositionAntinode({ x, y }, map));
      }
    }

    return acc;
  }

  public part2(input: Map): number {
    return getAntinodesWithResonance(input)!.length;
  }

  public main(): void {
    const input = this.parseInput(Deno.readTextFileSync("./src/day08.txt"));
    console.log("Day08");
    console.log("Part 1:", this.part1(input));
    console.log("Part 2:", this.part2(input));
  }

}


if(import.meta.main) {
	const solution = new Day08Solution();
	solution.main();
}


function getAntennaAtPosition({ x, y }: Coord2D, antennae: Antenna[]): Antenna | undefined {
  return antennae.find(antennae => 
    (antennae.x === x && antennae.y === y)
  );
}


function isPositionAntinode({ x, y }: Coord2D, map: Map): boolean {
  for(const antenna of map.antennae.all) {
    if(antenna.x === x && antenna.y === y) {
      continue;
    }
    const [_, translation] = getTranslation({ x, y }, antenna);
    const doubleTranslatedPosition = translation(antenna);

    if(!isPositionInBounds(doubleTranslatedPosition, map)) {
      continue;
    }

    if(getAntennaAtPosition(doubleTranslatedPosition, map.antennae[antenna.frequency])) {
      return true;
    }
  }

  return false;
}


function getTranslation(posA: Coord2D, posB: Coord2D): [Coord2D, (pos: Coord2D) => Coord2D] {
  const deltaX = posB.x - posA.x;
  const deltaY = posB.y - posA.y;
  const translation = ({ x, y }: Coord2D) => ({  x: x + deltaX, y: y + deltaY });

  return [{ x: deltaX, y: deltaY }, translation];
}


function isPositionInBounds(pos: Coord2D, bounds: Bounds2D): boolean {
  return pos.x >= 0 && pos.x < bounds.width && pos.y >= 0 && pos.y < bounds.height;
}


function getAntinodesWithResonance(map: Map): Coord2D[] {
  const antinodes: Coord2D[] = [];

  for(const firstAntenna of map.antennae.all) {
    for(const secondAntenna of map.antennae[firstAntenna.frequency]) {
      if(firstAntenna.x === secondAntenna.x && firstAntenna.y === secondAntenna.y) {
        continue;
      }

      const [{ x: deltaX, y: deltaY }, translation] = getTranslation(firstAntenna, secondAntenna);
      const inverseTranslation = ({ x, y }: Coord2D) => ({ x: x - deltaX, y: y - deltaY });

      let arcStartingPosition = inverseTranslation(firstAntenna);
      while(isPositionInBounds(arcStartingPosition, map)) {
        arcStartingPosition = inverseTranslation(arcStartingPosition);
      }

      const arcPositions = getPositionsOnArc(arcStartingPosition, map, translation);
      for(const arcPosition of arcPositions) {
        if(!antinodes.some(antinode => antinode.x === arcPosition.x && antinode.y === arcPosition.y)) {
          antinodes.push(arcPosition);
        }
      }
    }
  }

  return antinodes;
}


function getPositionsOnArc(initialPosition: Coord2D, bounds: Bounds2D, translation: (pos: Coord2D) => Coord2D): Coord2D[] {
  const positions: Coord2D[] = [];

  let cur = translation(initialPosition);

  while(isPositionInBounds(cur, bounds)) {
    positions.push(cur);
    cur = translation(cur);
  }

  return positions;
}
