# #085 C++

## Latest recorded verification

Latest extension checks:
- `.c++`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e632b2b.json).
- `.cc`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e6363.json).
- `.cp`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e6370.json).
- `.cxx`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e637878.json).
- `.h`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e68.json).
- `.h++`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e682b2b.json).
- `.hh`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e6868.json).
- `.hpp`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e687070.json).
- `.hxx`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e687878.json).
- `.inc`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e696e63.json).
- `.inl`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e696e6c.json).
- `.ipp`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e697070.json).
- `.tcc`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e746363.json).
- `.tpp`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e747070.json).
- `.txx`: Variant only. Main language status and other suffixes unchanged. [Evidence](verification/native_20261104_followup_2e747878.json).

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
| `.c++` | [hello.c++](variants/ext-c-2e632b2b/hello.c%2B%2B) syntax and behavior verified |
| `.cc` | [hello.cc](variants/ext-cc-2e6363/hello.cc) syntax and behavior verified |
| `.cp` | [hello.cp](variants/ext-cp-2e6370/hello.cp) syntax and behavior verified |
| `.cppm` | [hello.cppm](variants/ext-cppm-2e6370706d/hello.cppm) created; verification pending |
| `.cxx` | [hello.cxx](variants/ext-cxx-2e637878/hello.cxx) syntax and behavior verified |
| `.h` | [hello.h](variants/ext-h-2e68/hello.h) syntax and behavior verified |
| `.h++` | [hello.h++](variants/ext-h-2e682b2b/hello.h%2B%2B) syntax and behavior verified |
| `.hh` | [hello.hh](variants/ext-hh-2e6868/hello.hh) syntax and behavior verified |
| `.hpp` | [hello.hpp](variants/ext-hpp-2e687070/hello.hpp) syntax and behavior verified |
| `.hxx` | [hello.hxx](variants/ext-hxx-2e687878/hello.hxx) syntax and behavior verified |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) syntax and behavior verified |
| `.inl` | [hello.inl](variants/ext-inl-2e696e6c/hello.inl) syntax and behavior verified |
| `.ino` | [hello.ino](variants/ext-ino-2e696e6f/hello.ino) created; verification pending |
| `.ipp` | [hello.ipp](variants/ext-ipp-2e697070/hello.ipp) syntax and behavior verified |
| `.ixx` | [hello.ixx](variants/ext-ixx-2e697878/hello.ixx) created; verification pending |
| `.re` | [hello.re](variants/ext-re-2e7265/hello.re) created; verification pending |
| `.tcc` | [hello.tcc](variants/ext-tcc-2e746363/hello.tcc) syntax and behavior verified |
| `.tpp` | [hello.tpp](variants/ext-tpp-2e747070/hello.tpp) syntax and behavior verified |
| `.txx` | [hello.txx](variants/ext-txx-2e747878/hello.txx) syntax and behavior verified |