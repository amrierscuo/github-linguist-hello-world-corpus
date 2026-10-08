set(GREETING "Hello, World!")
configure_file(hello.h.in "${OUT}/hello.h" @ONLY)
