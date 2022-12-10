#include "StringUtils.hpp"


const bool StringUtils::stringContains(const std::string searchString, const std::string searchItem) {
	return searchString.find(searchItem) != std::string::npos;
}
