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


func Part1(input string) int {
	lines := strings.Split(input, "\n")

	incrementor := 0
	for _, line := range lines {
		var firstDigit, lastDigit int

		for _, c := range line {
			if !unicode.IsDigit(c) {
				continue
			}
			
			if firstDigit == 0 {
				firstDigit = int(c - '0')
			}

			lastDigit = int(c - '0')
		}

		totalNum := (firstDigit * 10) + lastDigit
		fmt.Printf("(%d) (%d) (%d)\n", firstDigit, lastDigit, totalNum)

		incrementor += totalNum
	}

	return incrementor
}


func Part2(input string) int {
	lines := strings.Split(input, "\n")

	incrementor := 0
	for _, line := range lines {
		var firstDigit, lastDigit int
		var setDigit = func(digit int) {
			if firstDigit == 0 {
				firstDigit = digit
			}

			lastDigit = digit
		}

		for i, c := range line {
			if unicode.IsDigit(c) {
				setDigit(int(c - '0'))
			} else {
				if i <= len(line) - 3 && line[i:i+3] == "one" {
					setDigit(1)
				} else if i <= len(line) - 3 && line[i:i+3] == "two" {
					setDigit(2)
				} else if i <= len(line) - 5 && line[i:i+5] == "three" {
					setDigit(3)
				} else if i <= len(line) - 4 && line[i:i+4] == "four" {
					setDigit(4)
				} else if i <= len(line) - 4 && line[i:i+4] == "five" {
					setDigit(5)
				} else if i <= len(line) - 3 && line[i:i+3] == "six" {
					setDigit(6)
				} else if i <= len(line) - 5 && line[i:i+5] == "seven" {
					setDigit(7)
				} else if i <= len(line) - 5 && line[i:i+5] == "eight" {
					setDigit(8)
				} else if i <= len(line) - 4 && line[i:i+4] == "nine" {
					setDigit(9)
				}
			}
		}

		totalNum := (firstDigit * 10) + lastDigit
		fmt.Printf("(%d) (%d) (%d)\n", firstDigit, lastDigit, totalNum)

		incrementor += totalNum
	}

	return incrementor
}
