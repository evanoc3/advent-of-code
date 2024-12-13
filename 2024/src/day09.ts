import type { ISolution } from "./common.ts";


interface DiskBlock {
	file?: number
	location: number
	size: number
}


export class Day09Solution implements ISolution<DiskBlock[], number, number> {

  public parseInput(text: string): DiskBlock[] {
		const diskMap: DiskBlock[] = [];
		let fileIndex = 0;
		let location = 0;

		for(let i = 0; i < text.length; i++) {
			const size = parseInt(text[i]);

			if(i % 2 == 0) {
				diskMap.push({ file: fileIndex++, location, size });
			}

			location += size;
		}

		return diskMap;
  }

  public part1(initialDiskMap: DiskBlock[]): number {
		const diskMap = compactFileBlocks(initialDiskMap);

		return calculateChecksum(diskMap);
  }

  public part2(diskMap: DiskBlock[]): number {
		const maxFileIndex = diskMap.at(-1)!.file!;

		for(let curFile = maxFileIndex; curFile >= 0; curFile--) {
			const file = getFile(diskMap, curFile)!;
			const emptySpace = findEmptySpaceForFile(diskMap, file);
			if(emptySpace) {
				const oldIndex = diskMap.indexOf(file);
				diskMap.splice(oldIndex, 1);

				const insertionIndex = diskMap.findIndex(block => block.location + block.size === emptySpace.location) + 1;

				diskMap.splice(insertionIndex, 0, {
					...file,
					location: emptySpace.location,
				});
			}
		}

		return calculateChecksum(diskMap);
  }

  public main(): void {
		const input = this.parseInput(
			Deno.readTextFileSync("./src/day09.txt")
		);
		console.log("Day09");
		console.log("Part 1:", this.part1(structuredClone(input)));
		console.log("Part 2:", this.part2(structuredClone(input)));
  }

}


if(import.meta.main) {
	new Day09Solution().main();
}


function calculateChecksum(diskMap: DiskBlock[]): number {
	const maxDiskSize = diskMap.at(-1)!.location + diskMap.at(-1)!.size;
	let acc = 0;

	for(let i = 0; i < maxDiskSize; i++) {
		const file = diskMap.find(block => i >= block.location && i < block.location + block.size);

		if(file) {
			acc += i * file.file!;
		}
	}
	return acc;
}


function getEmptySpaces(diskMap: DiskBlock[], max?: number): DiskBlock[] {
	const fileDistances: DiskBlock[] = [];
	for(let i = 0; i < diskMap.length - 1; i++) {
		const location = diskMap[i].location + diskMap[i].size;
		const size = diskMap[i + 1].location - location;
		if(size > 0) {
			fileDistances.push({ location, size });
			if(max && fileDistances.length >= max) {
				break;
			}
		}
	}

	return fileDistances;
}


function compactFileBlocks(diskMap: DiskBlock[]): DiskBlock[] {
	while(!isDiskMapCompact(diskMap)) {
		const poppedBlock = popLastFileBlock(diskMap);
		insertFileBlock(diskMap, poppedBlock);
	}

	return diskMap;
}


function isDiskMapCompact(diskMap: DiskBlock[]): boolean {
	return diskMap.every((fileBlock, i) => {
		const prevFileBlockEnd = (i > 0) ? diskMap[i - 1].location + diskMap[i - 1].size : 0;
		return fileBlock.location === prevFileBlockEnd;
	});
}


function popLastFileBlock(diskMap: DiskBlock[]): DiskBlock {
	const lastFileBlock = diskMap.at(-1)!;
	if(lastFileBlock.size === 1) {
		return {
			...diskMap.pop()!,
			location: -1
		};
	}

	lastFileBlock.size -= 1;
	return {
		file: lastFileBlock.file,
		location: -1,
		size: 1
	};
}


function insertFileBlock(diskMap: DiskBlock[], fileBlock: DiskBlock): void {
	const emptySpace = getEmptySpaces(diskMap, 1)[0];
	const insertionIndex = diskMap.findIndex(block => block.location + block.size === emptySpace.location) + 1;

	const prevFileBlock = diskMap[insertionIndex - 1];
	if(prevFileBlock.file === fileBlock.file) {
		prevFileBlock.size += fileBlock.size;
		return;
	}

	if(insertionIndex < diskMap.length) {
		const nextFileBlock = diskMap[insertionIndex];
		if(nextFileBlock.file === fileBlock.file) {
			nextFileBlock.location -= fileBlock.size;
			nextFileBlock.size += fileBlock.size;
			return;
		}
	}

	diskMap.splice(insertionIndex, 0, {
		...fileBlock,
		location: emptySpace.location
	});
}


function getFile(diskMap: DiskBlock[], searchFile: number): DiskBlock | undefined {
	for(let i = diskMap.length - 1; i >= 0; i--) {
		if(diskMap[i].file === searchFile) {
			return diskMap[i];
		}
	}
	return undefined;
}


function findEmptySpaceForFile(diskMap: DiskBlock[], file: DiskBlock): DiskBlock | undefined {
	const emptySpaces = getEmptySpaces(diskMap);

	for(let i = 0; i < emptySpaces.length; i++) {
		if(emptySpaces[i].location > file.location) {
			break;
		}

		if(emptySpaces[i].size >= file.size) {
			return emptySpaces[i];
		}
	}

	return undefined;
}
