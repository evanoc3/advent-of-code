package day_02

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed input.txt
var input string




func Solve() {
	fmt.Printf("day_02.Part1: %d\n", Part1(input))
	fmt.Printf("day_02.Part2: %d\n", Part2(input))
	fmt.Println()
}


func Part1(input string) int {
	games := parseInput(input)

	const maxRedCubes = 12
	const maxGreenCubes = 13
	const maxBlueCubes = 14

	incrementor := 0
	for i, g := range games {
		possible := true
		for _, r := range g.reveals {
			if r["red"] > maxRedCubes ||
				 r["green"] > maxGreenCubes ||
				 r["blue"] > maxBlueCubes {
				possible = false
				break
			}
		}
		if possible {
			incrementor += i + 1
		}
	}

	return incrementor
}


func Part2(input string) int {
	games := parseInput(input)

	incrementor := 0
	for _, g := range games {
		var minRedCubes, minGreenCubes, minBlueCubes int

		for _, r := range g.reveals {
			if redCubes, ok := r["red"]; ok && redCubes > minRedCubes {
				minRedCubes = r["red"]
			}
			if greenCubes, ok := r["green"]; ok && greenCubes > minGreenCubes {
				minGreenCubes = r["green"]
			}
			if blueCubes, ok := r["blue"]; ok && blueCubes > minBlueCubes {
				minBlueCubes = r["blue"]
			}
		}

		incrementor += (minRedCubes * minGreenCubes * minBlueCubes)
	}

	return incrementor
}


type game struct {
	reveals []map[string]int
}


func parseInput(input string) []game {
	lines := strings.Split(input, "\n")

	games := make([]game, 0, len(lines))

	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		line = line[strings.Index(line, ": ")+2:]
		revealStrings := strings.Split(line, "; ")

		g := game{
			reveals: make([]map[string]int, 0, len(revealStrings)),
		}

		for _, revealString := range revealStrings {
			reveal := make(map[string]int)

			colourStrings := strings.Split(revealString, ", ")

			for _, colourString := range colourStrings {
				subparts := strings.Split(colourString, " ")
				num, _ := strconv.ParseInt(subparts[0], 10, 64)
				colour := subparts[1]

				reveal[colour] = int(num)
			}

			g.reveals = append(g.reveals, reveal)
		}

		games = append(games, g)
	}
	return games
}
