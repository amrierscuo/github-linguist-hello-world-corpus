set(GREETING "Hello, World!")
configure_file(hello.cmake.in "${OUT}/hello.cmake" @ONLY)
