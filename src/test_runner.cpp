#define CATCH_CONFIG_RUNNER
#include <catch.hpp>
#include <iostream>

int main(int argc, char* argv[]) {
  #ifdef TEST_ENV
		std::cout << "Test: Hello, World! This is a test" << std::endl;
	#endif

  return Catch::Session().run(argc, argv);
}
