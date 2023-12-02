package day_01

import (
	_ "embed"
	"fmt"
	"strings"
	"unicode"
)

//go:embed input.txt
var input string


func Solve() {
	fmt.Printf("day_01.part1: %d\n", Part1(input))
}


func Part1(input string) uint64 {
	lines := strings.Split(input, "\n")

	incrementor := uint64(0)
	for _, line := range lines {
		var firstDigit, lastDigit uint64

		for _, c := range line {
			if !unicode.IsDigit(c) {
				continue
			}
			
			if firstDigit == 0 {
				firstDigit = uint64(c - '0')
			}

			lastDigit = uint64(c - '0')
		}

		totalNum := (firstDigit * 10) + lastDigit
		fmt.Printf("(%d) (%d) (%d)\n", firstDigit, lastDigit, totalNum)

		incrementor += totalNum
	}

	return incrementor
}
