package day_01

import (
	_ "embed"
	"testing"

	"github.com/stretchr/testify/require"
)

//go:embed part1_sample_input.txt
var part1_sample_input string
//go:embed part2_sample_input.txt
var part2_sample_input string


func TestPart1(t *testing.T) {
	require := require.New(t)

	// test on smaple input
	require.Equal(142, int(Part1(part1_sample_input)))

	// test on real input
	require.Equal(56397, int(Part1(input)))
}


func TestPart2(t *testing.T) {
	require := require.New(t)

	//test on sample input
	require.Equal(281, Part2(part2_sample_input))

	// test on real input
	require.Equal(55701, Part2(input))
}
