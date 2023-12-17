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

	// test against sample input
	require.Equal(4361, Part1(sampleInput))
}

func TestPart1WithActualInput(t *testing.T) {
	require := require.New(t)

	// test against sample input
	require.Equal(536202, Part1(input))
}
