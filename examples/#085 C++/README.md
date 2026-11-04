# #085 C++

Stampare esattamente Hello, World! seguito da newline con std::cout in C++17.

## Toolchain

g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Commands and procedure

Da Linux/WSL:

```sh
mkdir -p build
g++ --version
g++ -std=c++17 -Wall -Wextra -Werror -o build/hello hello.cpp
./build/hello
```

## Expected result

Exit 0; exit program 0, stdout Hello, World! plus newline.

## Status

syntax and behavior verified.

Compilatore C++ e programma realmente eseguiti; nessun interprete sostitutivo.

Actual verification of 2026-10-08T11:33:37.086545+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.open-std.org/jtc1/sc22/wg21/](https://www.open-std.org/jtc1/sc22/wg21/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cpp` | [hello.cpp](hello.cpp), [consumer.cpp](variants/ext-cppm-2e6370706d/consumer.cpp), [consumer.cpp](variants/ext-h-2e68/consumer.cpp), [consumer.cpp](variants/ext-h-2e682b2b/consumer.cpp), [consumer.cpp](variants/ext-hh-2e6868/consumer.cpp), [consumer.cpp](variants/ext-hpp-2e687070/consumer.cpp), [consumer.cpp](variants/ext-hxx-2e687878/consumer.cpp), [consumer.cpp](variants/ext-inc-2e696e63/consumer.cpp), [consumer.cpp](variants/ext-inl-2e696e6c/consumer.cpp), [consumer.cpp](variants/ext-ipp-2e697070/consumer.cpp), [consumer.cpp](variants/ext-ixx-2e697878/consumer.cpp), [consumer.cpp](variants/ext-tcc-2e746363/consumer.cpp), [consumer.cpp](variants/ext-tpp-2e747070/consumer.cpp), [consumer.cpp](variants/ext-txx-2e747878/consumer.cpp) created; verification pending |
| `.c++` | [hello.c++](variants/ext-c-2e632b2b/hello.c%2B%2B) created; verification pending |
| `.cc` | [hello.cc](variants/ext-cc-2e6363/hello.cc) created; verification pending |
| `.cp` | [hello.cp](variants/ext-cp-2e6370/hello.cp) created; verification pending |
| `.cppm` | [hello.cppm](variants/ext-cppm-2e6370706d/hello.cppm) created; verification pending |
| `.cxx` | [hello.cxx](variants/ext-cxx-2e637878/hello.cxx) created; verification pending |
| `.h` | [hello.h](variants/ext-h-2e68/hello.h) created; verification pending |
| `.h++` | [hello.h++](variants/ext-h-2e682b2b/hello.h%2B%2B) created; verification pending |
| `.hh` | [hello.hh](variants/ext-hh-2e6868/hello.hh) created; verification pending |
| `.hpp` | [hello.hpp](variants/ext-hpp-2e687070/hello.hpp) created; verification pending |
| `.hxx` | [hello.hxx](variants/ext-hxx-2e687878/hello.hxx) created; verification pending |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) created; verification pending |
| `.inl` | [hello.inl](variants/ext-inl-2e696e6c/hello.inl) created; verification pending |
| `.ino` | [hello.ino](variants/ext-ino-2e696e6f/hello.ino) created; verification pending |
| `.ipp` | [hello.ipp](variants/ext-ipp-2e697070/hello.ipp) created; verification pending |
| `.ixx` | [hello.ixx](variants/ext-ixx-2e697878/hello.ixx) created; verification pending |
| `.re` | [hello.re](variants/ext-re-2e7265/hello.re) created; verification pending |
| `.tcc` | [hello.tcc](variants/ext-tcc-2e746363/hello.tcc) created; verification pending |
| `.tpp` | [hello.tpp](variants/ext-tpp-2e747070/hello.tpp) created; verification pending |
| `.txx` | [hello.txx](variants/ext-txx-2e747878/hello.txx) created; verification pending |
