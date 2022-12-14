#include "FileUtils.hpp"
#include <fstream>
#include <iterator>


const std::string Utils::getFileContents(const std::filesystem::path filePath) {
	std::ifstream ifs(filePath.string());
	const auto fileContent = std::string(std::istreambuf_iterator<char>(ifs), std::istreambuf_iterator<char>());
	ifs.close();
	return fileContent;
}
