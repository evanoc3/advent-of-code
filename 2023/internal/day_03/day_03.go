package day_03

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

//go:embed input.txt
var input string


func Solve() {
	fmt.Printf("day_03.Part1: %d\n", Part1(input))
	fmt.Printf("day_03.Part2: %d\n", Part2(input))
}


type coord struct {
	X int
	Y int
}

type parsedInput struct {
	partNumbers []*partNumber
	symbolCoords []*symbol
}

type symbol struct {
	coord
	Symbol rune
}

type partNumber struct {
	coord
	Value string 
}

func (pn *partNumber) Int() int {
	i, _ := strconv.ParseInt(pn.Value, 10, 64)
	return int(i)
}

func Part1(input string) int {
	inp := parseInput(input)

	var acc int
	for _, pn := range inp.partNumbers {
		// define the rectangle around the part number which we cehck for a symbol within
		x1 := pn.X - 1
		x2 := pn.X + len(pn.Value)
		y1 := pn.Y - 1
		y2 := pn.Y + 1

		for _, sym := range inp.symbolCoords {
			if sym.X >= x1 && sym.X <= x2 && sym.Y >= y1 && sym.Y <= y2 {
				acc += pn.Int()
				break
			}
		}
	}

	return acc
}

func parseInput(input string) parsedInput {
	lines := strings.Split(input, "\n")

	inp := parsedInput{
		partNumbers: make([]*partNumber, 0),
		symbolCoords: make([]*symbol, 0),
	}

	for y, line := range lines {
		var pn *partNumber

		for x, c := range line {
			if unicode.IsDigit(c) {
				if pn == nil {
					pn = &partNumber{
						coord: coord{
							X: x,
							Y: y,
						},
						Value: string(c),
					}
				} else {
					pn.Value += string(c)
				}
			} else {
				if c != '.' {
					inp.symbolCoords = append(inp.symbolCoords, &symbol{
						coord: coord{
							X: x,
							Y: y,
						},
						Symbol: c,
					})
				}
			
				if pn != nil {
					inp.partNumbers = append(inp.partNumbers, pn)
					pn = nil
				}
			}
		}

		if pn != nil {
			inp.partNumbers = append(inp.partNumbers, pn)
			pn = nil
		}
	}

	return inp
}


func Part2(input string) int {
	inp := parseInput(input)
	gears := getGears(inp)

	var acc int
	for _, gear := range gears {
		acc += gear.AdjacentNumbers[0].Int() * gear.AdjacentNumbers[1].Int()
	}

	return acc
}


type gear struct {
	Symbol *symbol
	AdjacentNumbers []*partNumber
}

type rect struct {
	coord
	W int
	H int
}

func getGears(inp parsedInput) []*gear {
	gears := make([]*gear, 0)

	for _, sym := range inp.symbolCoords {
		if sym.Symbol != '*' {
			continue
		}

		symRect := rect{
			coord: coord{
				X: sym.X - 1,
				Y: sym.Y - 1,
			},
			W: 3,
			H: 3,
		}

		adjacentParts := make([]*partNumber, 0)

		for _, pn := range inp.partNumbers {
			pnRect := rect{
				coord: coord{
					X: pn.X,
					Y: pn.Y,
				},
				W: len(pn.Value),
				H: 1,
			}

			if rectsIntersect(symRect, pnRect) {
				adjacentParts = append(adjacentParts, pn)
			}
		}

		if len(adjacentParts) == 2 {
			gears = append(gears, &gear{
				Symbol: sym,
				AdjacentNumbers: adjacentParts,
			})
		}
	}

	return gears
}

func rectsIntersect(rect1, rect2 rect) bool {
	x1 := rect1.X
	x2 := rect1.X + rect1.W
	y1 := rect1.Y
	y2 := rect1.Y + rect1.H

	x3 := rect2.X
	x4 := rect2.X + rect2.W
	y3 := rect2.Y
	y4 := rect2.Y + rect2.H

	return x1 < x4 && x2 > x3 && y1 < y4 && y2 > y3
}
