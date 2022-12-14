#include <sstream>
#include <regex>
#include <algorithm>
#include "solution.hpp"


using namespace Year2022::Day07;


Solution::Solution()
	: mInputFilePath(std::filesystem::path(__FILE__).replace_filename("input.txt")) {
}


void Solution::parseInput(const std::string& rawInput) {
	std::stringstream inputStream(rawInput);
	mInput = std::make_unique<Dir>("/");
	Dir* cur = mInput.get();

	const std::regex cdRegex(R"(\$ cd ((?:\.\.|\w+|\/)))");
	const std::regex fileRegex(R"((\d+) ((?:\w|\.)+))");
	const std::regex dirRegex(R"(dir (\w+))");

	std::string line;
	while(std::getline(inputStream, line)) {
		std::smatch matches;
		
		// cd commands
		if(regex_search(line, matches, cdRegex)) {
			const auto destStr = matches[1].str();

			if(destStr == ".." && cur->parent != nullptr) {
				cur = cur->parent;
			}
			else if(auto newCwd = cur->getSubDir(destStr)) {
				cur = newCwd;
			}
		}

		// ls commands
		else if(line == "$ ls") {
			continue;
		}

		// file regex
		else if(regex_search(line, matches, fileRegex)) {
			const auto fileSize = std::stoi(matches[1].str());
			const auto fileName = matches[2].str();
			cur->files.emplace_back( std::make_unique<File>(fileName, fileSize) );
		}

		// dir regex
		else if(regex_search(line, matches, dirRegex)) {
			const auto dirName = matches[1].str();
			cur->subDirs.emplace_back( std::make_unique<Dir>(dirName) );
			cur->subDirs.back()->parent = cur;
		}
	}
}


File::File(const std::string name, const int size)
	: name(name)
	, size(size) {
}


Dir::Dir(const std::string name)
	: name(name) {
}


int Dir::getSize() const {
	int accumulator{ 0 };

	for(const auto& file : files) {
		accumulator += file->size;
	}

	for(const auto& subDir : subDirs) {
		accumulator += subDir->getSize();
	}

	return accumulator;
}


Dir* Dir::getSubDir(const std::string& searchDirName) const {
	for(auto& subDir : subDirs) {
		if(subDir->name == searchDirName) {
			return subDir.get();
		}
	}
	return nullptr;
}


const int Solution::part1() const {
	int accumulator = 0;

	const auto dirsOver100Kb = getDirsUnder100Kb(mInput.get());
	for(const auto& dir : dirsOver100Kb) {
		if(dir != nullptr) {
			accumulator += dir->getSize();
		}
	}

	return accumulator;
}


const std::vector<const Dir*> Solution::getDirsUnder100Kb(const Dir* dir) const {
	if(dir == nullptr) {
		return {};
	}

	const auto dirIsUnder100Kb = dir->getSize() <= 100000;

	std::vector<const Dir*> dirsUnder100Kb( dirIsUnder100Kb ? 1 : 0 );

	if(dirIsUnder100Kb) {
		dirsUnder100Kb.emplace_back(dir);
	}

	for(const auto& subDir : dir->subDirs) {
		const auto subDirsUnder100Kb = getDirsUnder100Kb(subDir.get());

		dirsUnder100Kb.reserve( dirsUnder100Kb.size() + subDirsUnder100Kb.size() );
		for(const auto& subDirPtr : subDirsUnder100Kb) {
			dirsUnder100Kb.emplace_back(subDirPtr);
		}
	}

	return dirsUnder100Kb;
}


const int Solution::part2() const {
	const auto unusedSpace = 70000000 - mInput->getSize();
	const auto spaceNeeded = 30000000 - unusedSpace;

	// remove nullptrs from the vector of arrays
	auto dirs = getDirsOverSize(mInput.get(), spaceNeeded);
	dirs.erase(std::remove_if(dirs.begin(), dirs.end(), [](const auto& dir) {
		return dir == nullptr;
	}));
	// sort it by dir size
	std::sort(dirs.begin(), dirs.end(), Solution::compareDirSizes);

	// now the smallest directory of sufficient size will be at the start of the vector
	return dirs.front()->getSize();
}


const std::vector<const Dir*> Solution::getDirsOverSize(const Dir* dir, const int minSize) const {
	if(dir == nullptr) {
		return {};
	}

	const auto dirIsOverSize = dir->getSize() >= minSize;

	std::vector<const Dir*> allDirsOverSize( dirIsOverSize ? 1 : 0 );

	if(dirIsOverSize) {
		allDirsOverSize.emplace_back(dir);
	}

	for(const auto& subDir : dir->subDirs) {
		const auto subDirsOverSize = getDirsOverSize(subDir.get(), minSize);

		allDirsOverSize.reserve( allDirsOverSize.size() + subDirsOverSize.size() );
		for(const auto& subDir : subDirsOverSize) {
			if(subDir != nullptr) {
				allDirsOverSize.emplace_back(subDir);
			}
		}
	}

	return allDirsOverSize;
}


bool Solution::compareDirSizes(const Dir*& dir1, const Dir*& dir2) {
	return dir1->getSize() <= dir2->getSize();
}
