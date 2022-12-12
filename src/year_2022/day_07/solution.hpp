#pragma once
#include <string>
#include <vector>
#include <memory>
#include <functional>

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

		Dir* parent;
		const std::string name;
		std::vector<DirPtr> subDirs;
		std::vector<FilePtr> files;

		int getSize() const;
		Dir* getSubDir(const std::string dirName) const;
	};


	using Input = DirPtr;
	
	
	class Solution final {
	public:
		~Solution() = default;
		
		void getInput();
		const int part1(const Input& input) const;
		const int part2(const Input& input) const;

		const std::vector<const Dir*> getDirsUnder100Kb(const Dir* rootDir) const;
		const std::vector<const Dir*> getDirsOverSize(const Dir* dir, const int minSize) const;

		static bool compareDirSizes(const Dir*& dir1, const Dir*& dir2);

		Input input{ nullptr };
	};
	
}
