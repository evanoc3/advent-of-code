#include <catch.hpp>
#include "utils/FileUtils.hpp"
#include "solution.hpp"


using namespace Year2022::Day07;


namespace Year2022::Day07 {

	class SolutionTests {
	public:
		SolutionTests()
			: mSolution(std::make_unique<Solution>())
			, mSampleRawInput("$ cd /\n"
												"$ ls\n"
												"dir a\n"
												"14848514 b.txt\n"
												"8504156 c.dat\n"
												"dir d\n"
												"$ cd a\n"
												"$ ls\n"
												"dir e\n"
												"29116 f\n"
												"2557 g\n"
												"62596 h.lst\n"
												"$ cd e\n"
												"$ ls\n"
												"584 i\n"
												"$ cd ..\n"
												"$ cd ..\n"
												"$ cd d\n"
												"$ ls\n"
												"4060174 j\n"
												"8033020 d.log\n"
												"5626152 d.ext\n"
												"7214296 k\n")
			, mActualRawInput(Utils::getFileContents(mSolution->mInputFilePath)) {
		}

		void injectSampleInput() const {
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
			mSolution->mInput.swap(newInput);
		}
	
		const std::unique_ptr<Solution> mSolution;
		const std::string mSampleRawInput;
		const std::string mActualRawInput;
	};
	
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day07::Solution::parseInput", "[Year2022][Day07][parseInput]")
{

	GIVEN("Sample Raw Input")
	{
		mSolution->parseInput(mSampleRawInput);
	}

	GIVEN("Actual Raw Input")
	{
		mSolution->parseInput(mActualRawInput);

		REQUIRE( mSolution->mInput->name == "/" );

		REQUIRE( mSolution->mInput->files.size() == 1 );
		REQUIRE( mSolution->mInput->files[0]->name == "vjw" );
		REQUIRE( mSolution->mInput->files[0]->size == 132067 );

		REQUIRE( mSolution->mInput->subDirs.size() == 7 );
		REQUIRE( mSolution->mInput->subDirs[0]->name == "fnsvfbzt" );
		REQUIRE( mSolution->mInput->subDirs[1]->name == "hqdssf" );
		REQUIRE( mSolution->mInput->subDirs[2]->name == "jwphbz" );
		REQUIRE( mSolution->mInput->subDirs[3]->name == "lncqsmj" );
		REQUIRE( mSolution->mInput->subDirs[4]->name == "mhqs" );
		REQUIRE( mSolution->mInput->subDirs[5]->name == "trwqgzsb" );
		REQUIRE( mSolution->mInput->subDirs[6]->name == "wbsph" );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day07::Solution::part1", "[Year2022][Day07][part1]")
{
	GIVEN("Sample input")
	{
		mSolution->parseInput(mSampleRawInput);
		// injectSampleInput();
		REQUIRE( mSolution->part1() == 95437 );
	}
	
	GIVEN("Real input")
	{
		mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part1() == 2031851 );
	}
}


TEST_CASE_METHOD(SolutionTests, "Year2022::Day07::Solution::part2", "[Year2022][Day07][part2]")
{
	GIVEN("Sample input")
	{
		mSolution->parseInput(mSampleRawInput);
		// injectSampleInput();
		REQUIRE( mSolution->part2() == 24933642 );
	}
	
	GIVEN("Real input")
	{
		mSolution->parseInput(mActualRawInput);
		REQUIRE( mSolution->part2() == 2568781 );
	}
}
