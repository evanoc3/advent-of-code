export interface ISolution<I, T1, T2> {
	/** Should return some parsed structure representing the input to the 2 parts of the problem. */
	parseInput(text: string): I;

	/** Computes and returns the answer to part 1 of the problem. */
	part1(input: I): T1;

	/** Computes and returns the answer to part 2 of the problem. */
	part2(input: I): T2;

	/** Called when the solution module is run directly. Should print out the answers to the two parts of the problem. */
	main(): void;
}
