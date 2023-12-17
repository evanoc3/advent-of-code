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
