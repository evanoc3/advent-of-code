package day_01

import (
	_ "embed"
	"testing"

	"github.com/stretchr/testify/require"
)

//go:embed sample_input.txt
var sample_input string


func TestPart1(t *testing.T) {
	require := require.New(t)

	// test on smaple input
	require.EqualValues(142, Part1(sample_input))

	// test on real input
	require.EqualValues(56397, Part1(input))
}
