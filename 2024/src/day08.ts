import type { ISolution, Position2D } from "./common.ts";


interface Map {
	width: number
	height: number
	antennae: { [key: string]: Antenna[] }
}


interface Antenna extends Position2D {
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


function getAntennaAtPosition({ x, y }: Position2D, antennae: Antenna[]): Antenna | undefined {
  return antennae.find(antennae => 
    (antennae.x === x && antennae.y === y)
  );
}


function isPositionAntinode({ x, y }: Position2D, map: Map): boolean {
  for(const antenna of map.antennae.all) {
    if(antenna.x === x && antenna.y === y) {
      continue;
    }
    const [_, translation] = getTranslation({ x, y }, antenna);
    const doubleTranslatedPosition = translation(antenna);

    if(!isPositionInBounds(doubleTranslatedPosition, { x: map.width, y: map.height })) {
      continue;
    }

    if(getAntennaAtPosition(doubleTranslatedPosition, map.antennae[antenna.frequency])) {
      return true;
    }
  }

  return false;
}


function getTranslation(posA: Position2D, posB: Position2D): [Position2D, (pos: Position2D) => Position2D] {
  const deltaX = posB.x - posA.x;
  const deltaY = posB.y - posA.y;
  const translation = ({ x, y }: Position2D) => ({  x: x + deltaX, y: y + deltaY });

  return [{ x: deltaX, y: deltaY }, translation];
}


function isPositionInBounds(pos: Position2D, bounds: Position2D): boolean {
  return pos.x >= 0 && pos.x < bounds.x && pos.y >= 0 && pos.y < bounds.y;
}


function getAntinodesWithResonance(map: Map): Position2D[] {
  const antinodes: Position2D[] = [];

  for(const firstAntenna of map.antennae.all) {
    for(const secondAntenna of map.antennae[firstAntenna.frequency]) {
      if(firstAntenna.x === secondAntenna.x && firstAntenna.y === secondAntenna.y) {
        continue;
      }

      const [{ x: deltaX, y: deltaY }, translation] = getTranslation(firstAntenna, secondAntenna);
      const inverseTranslation = ({ x, y }: Position2D) => ({ x: x - deltaX, y: y - deltaY });

      let arcStartingPosition = inverseTranslation(firstAntenna);
      while(isPositionInBounds(arcStartingPosition, { x: map.width, y: map.height })) {
        arcStartingPosition = inverseTranslation(arcStartingPosition);
      }

      const arcPositions = getPositionsOnArc(arcStartingPosition, { x: map.width, y: map.height }, translation);
      for(const arcPosition of arcPositions) {
        if(!antinodes.some(antinode => antinode.x === arcPosition.x && antinode.y === arcPosition.y)) {
          antinodes.push(arcPosition);
        }
      }
    }
  }

  return antinodes;
}


function getPositionsOnArc(initialPosition: Position2D, bounds: Position2D, translation: (pos: Position2D) => Position2D): Position2D[] {
  const positions: Position2D[] = [];

  let cur = translation(initialPosition);

  while(isPositionInBounds(cur, bounds)) {
    positions.push(cur);
    cur = translation(cur);
  }

  return positions;
}
