package day_02

import (
	_ "embed"

	"testing"

	"github.com/stretchr/testify/require"
)

//go:embed sample_input.txt
var sample_input string


func TestPart1(t *testing.T) {
	require := require.New(t)

	// test on sample input
	require.Equal(8, Part1(sample_input))

	// test on real input
	require.Equal(2632, Part1(input))
}


func TestPart2(t *testing.T) {
	require := require.New(t)

	// test on sample input
	require.Equal(2286, Part2(sample_input))

	// test on real input
	require.Equal(69629, Part2(input))
}
