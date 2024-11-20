package day04

import (
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string


func Solve() {
	fmt.Printf("day_04.Part1: %d\n", Part1(input))
	fmt.Println()
}


func Part1(input string) int {
	return 0
}
