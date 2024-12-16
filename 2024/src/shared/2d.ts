export interface Coord2D {
	x: number
	y: number
}

export interface Bounds2D {
	width: number
	height: number
}

export function coordIsWithinBounds(coord: Coord2D, bounds: Bounds2D): boolean {
	return coord.x >= 0 && coord.x < bounds.width && coord.y >= 0 && coord.y < bounds.height;
}

export function coordsAreAdjacent(posA: Coord2D, posB: Coord2D): boolean {
	return Math.abs(posA.x - posB.x) + Math.abs(posA.y - posB.y) === 1;
}

export function coordsAreEqual(coordA: Coord2D, coordB: Coord2D): boolean {
	return coordA.x === coordB.x && coordA.y === coordB.y;
}

export type Matrix2D = number[][];

export enum Direction {
	North = "n",
	NorthEast = "ne",
	East = "e",
	SouthEast = "se",
	South = "s",
	SouthWest = "sw",
	West = "w",
	NorthWest = "nw"
}

export interface Vector2D extends Coord2D {
	direction: Direction;
};

export function vectorsAreEqual(vec: Vector2D, vecB: Vector2D): boolean {
	return coordsAreEqual(vec, vecB) && vec.direction === vecB.direction;
}

export const directionTranslations: Record<Direction, (p: Coord2D, n?: number) => Coord2D> = {
	[Direction.NorthWest]: (pos: Coord2D, n?: number) => ({ x: pos.x - (n ?? 1), y: pos.y - (n ?? 1) }),
	[Direction.North]:     (pos: Coord2D, n?: number) => ({ x: pos.x, y: pos.y - (n ?? 1) }),
	[Direction.NorthEast]: (pos: Coord2D, n?: number) => ({ x: pos.x + (n ?? 1), y: pos.y - (n ?? 1) }),
	[Direction.East]:      (pos: Coord2D, n?: number) => ({ x: pos.x + (n ?? 1), y: pos.y }),
	[Direction.SouthEast]: (pos: Coord2D, n?: number) => ({ x: pos.x + (n ?? 1), y: pos.y + (n ?? 1) }),
	[Direction.South]:     (pos: Coord2D, n?: number) => ({ x: pos.x, y: pos.y + (n ?? 1) }),
	[Direction.SouthWest]: (pos: Coord2D, n?: number) => ({ x: pos.x - (n ?? 1), y: pos.y + (n ?? 1) }),
	[Direction.West]:      (pos: Coord2D, n?: number) => ({ x: pos.x - (n ?? 1), y: pos.y })
};
