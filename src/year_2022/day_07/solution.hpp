#pragma once

#include <vector>
#include <memory>
#include "utils/ISolution.hpp"


namespace Year2022::Day07 {

	struct Dir;
	using DirPtr = std::unique_ptr<Dir>;
	struct File;
	using FilePtr = std::unique_ptr<File>;


	struct File {
	public:
		File(const std::string name, const int size);

		const std::string name;
		const int size;
	};

	struct Dir {
	public:
		Dir(const std::string name);

		int getSize() const;
		Dir* getSubDir(const std::string& dirName) const;

		Dir* parent;
		const std::string name;
		std::vector<DirPtr> subDirs;
		std::vector<FilePtr> files;
	};


	using Input = DirPtr;
	
	
	class Solution final : public IParseInput<void> 
											 , public ISolution<const int, const int> {
	public:
		Solution();
		~Solution() = default;
		
		// IParseInput
		void parseInput(const std::string& rawInput);

		// ISolution
		const int part1() const;
		const int part2() const;

		// Public Methods
		const std::vector<const Dir*> getDirsUnder100Kb(const Dir* rootDir) const;
		const std::vector<const Dir*> getDirsOverSize(const Dir* dir, const int minSize) const;
		static bool compareDirSizes(const Dir*& dir1, const Dir*& dir2);

		// Member Variables
		Input mInput{ nullptr };
		const std::filesystem::path mInputFilePath;
	};
	
}
