#pragma once

#include <string>
#include <filesystem>


namespace Utils {

	const std::string getFileContents(const std::filesystem::path filePath);

}
