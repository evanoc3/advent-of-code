#include <catch.hpp>
#include "solution.hpp"


using namespace Year2022::Day07;


namespace Year2022::Day07 {

	class SolutionTests {
	public:
		SolutionTests()
			: solution(std::make_unique<Solution>()) {
		}

		void injectSampleInput() const;
		
		std::unique_ptr<Solution> solution;
	};

}


void SolutionTests::injectSampleInput() const {
	auto newInput = std::make_unique<Dir>("/");

	// / directory
	Dir* cur = newInput.get();
	cur->files.push_back( std::make_unique<File>("b.txt", 14848514) );
	cur->files.push_back( std::make_unique<File>("c.dat", 8504156) );
	cur->subDirs.push_back( std::make_unique<Dir>("a") );
	cur->subDirs.push_back( std::make_unique<Dir>("d") );

	// /a directory
	cur = cur->getSubDir("a");
	cur->files.push_back( std::make_unique<File>("f", 29116) );
	cur->files.push_back( std::make_unique<File>("g", 2557) );
	cur->files.push_back( std::make_unique<File>("h.lst", 62596) );
	cur->subDirs.push_back( std::make_unique<Dir>("e") );

	// /a/e directory
	cur = cur->getSubDir("e");
	cur->files.push_back( std::make_unique<File>("i", 584) );

	// /d directory
	cur = newInput->getSubDir("d");
	cur->files.push_back( std::make_unique<File>("j", 4060174) );
	cur->files.push_back( std::make_unique<File>("d.log", 8033020) );
	cur->files.push_back( std::make_unique<File>("d.ext", 5626152) );
	cur->files.push_back( std::make_unique<File>("k", 7214296) );

	// inject the new input into solution
	solution->input.swap(newInput);
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day07::Solution::getInput", "[Year2022][Day07][getInput]")
{
	solution->getInput();

	REQUIRE( solution->input->name == "/" );

	REQUIRE( solution->input->files.size() == 1 );
	REQUIRE( solution->input->files[0]->name == "vjw" );
	REQUIRE( solution->input->files[0]->size == 132067 );

	REQUIRE( solution->input->subDirs.size() == 7 );
	REQUIRE( solution->input->subDirs[0]->name == "fnsvfbzt" );
	REQUIRE( solution->input->subDirs[1]->name == "hqdssf" );
	REQUIRE( solution->input->subDirs[2]->name == "jwphbz" );
	REQUIRE( solution->input->subDirs[3]->name == "lncqsmj" );
	REQUIRE( solution->input->subDirs[4]->name == "mhqs" );
	REQUIRE( solution->input->subDirs[5]->name == "trwqgzsb" );
	REQUIRE( solution->input->subDirs[6]->name == "wbsph" );
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day07::Solution::part1", "[Year2022][Day07][part1]")
{
	GIVEN("Sample input")
	{
		injectSampleInput();

		REQUIRE( solution->part1() == 95437 );
	}
	
	GIVEN("Real input")
	{
		solution->getInput();

		REQUIRE( solution->part1() == 2031851 );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day07::Solution::part2", "[Year2022][Day07][part2]")
{
	GIVEN("Sample input")
	{
		injectSampleInput();

		REQUIRE( solution->part2() == 24933642 );
	}
	
	GIVEN("Real input")
	{
		solution->getInput();
		
		REQUIRE( solution->part2() == 2568781 );
	}
}
