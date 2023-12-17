package day_03

import (
	_ "embed"
	"testing"

	"github.com/stretchr/testify/require"
)

//go:embed sample_input.txt
var sampleInput string


func TestPart1WithSampleInput(t *testing.T) {
	require := require.New(t)

	require.Equal(4361, Part1(sampleInput))
}


func TestPart1WithActualInput(t *testing.T) {
	require := require.New(t)

	require.Equal(536202, Part1(input))
}


func TestPart2WithSampleInput(t *testing.T) {
	require := require.New(t)

	require.Equal(467835, Part2(sampleInput))
}


func TestPart2WithActualInput(t *testing.T) {
	require := require.New(t)

	require.Equal(78272573, Part2(input))
}
