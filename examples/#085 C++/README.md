# #085 C++

Stampare esattamente Hello, World! seguito da newline con std::cout in C++17.

## Toolchain

g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Comandi e procedura

Da Linux/WSL:

```sh
mkdir -p build
g++ --version
g++ -std=c++17 -Wall -Wextra -Werror -o build/hello hello.cpp
./build/hello
```

## Risultato atteso

Compilazione exit 0; programma exit 0, stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Compilatore C++ e programma realmente eseguiti; nessun interprete sostitutivo.

Verifica effettiva del 2026-10-08T11:33:37.086545+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.open-std.org/jtc1/sc22/wg21/](https://www.open-std.org/jtc1/sc22/wg21/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cpp` | [hello.cpp](hello.cpp), [consumer.cpp](variants/ext-cppm-2e6370706d/consumer.cpp), [consumer.cpp](variants/ext-h-2e68/consumer.cpp), [consumer.cpp](variants/ext-h-2e682b2b/consumer.cpp), [consumer.cpp](variants/ext-hh-2e6868/consumer.cpp), [consumer.cpp](variants/ext-hpp-2e687070/consumer.cpp), [consumer.cpp](variants/ext-hxx-2e687878/consumer.cpp), [consumer.cpp](variants/ext-inc-2e696e63/consumer.cpp), [consumer.cpp](variants/ext-inl-2e696e6c/consumer.cpp), [consumer.cpp](variants/ext-ipp-2e697070/consumer.cpp), [consumer.cpp](variants/ext-ixx-2e697878/consumer.cpp), [consumer.cpp](variants/ext-tcc-2e746363/consumer.cpp), [consumer.cpp](variants/ext-tpp-2e747070/consumer.cpp), [consumer.cpp](variants/ext-txx-2e747878/consumer.cpp) creato, verifiche pendenti |
| `.c++` | [hello.c++](variants/ext-c-2e632b2b/hello.c%2B%2B) creato, verifiche pendenti |
| `.cc` | [hello.cc](variants/ext-cc-2e6363/hello.cc) creato, verifiche pendenti |
| `.cp` | [hello.cp](variants/ext-cp-2e6370/hello.cp) creato, verifiche pendenti |
| `.cppm` | [hello.cppm](variants/ext-cppm-2e6370706d/hello.cppm) creato, verifiche pendenti |
| `.cxx` | [hello.cxx](variants/ext-cxx-2e637878/hello.cxx) creato, verifiche pendenti |
| `.h` | [hello.h](variants/ext-h-2e68/hello.h) creato, verifiche pendenti |
| `.h++` | [hello.h++](variants/ext-h-2e682b2b/hello.h%2B%2B) creato, verifiche pendenti |
| `.hh` | [hello.hh](variants/ext-hh-2e6868/hello.hh) creato, verifiche pendenti |
| `.hpp` | [hello.hpp](variants/ext-hpp-2e687070/hello.hpp) creato, verifiche pendenti |
| `.hxx` | [hello.hxx](variants/ext-hxx-2e687878/hello.hxx) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) creato, verifiche pendenti |
| `.inl` | [hello.inl](variants/ext-inl-2e696e6c/hello.inl) creato, verifiche pendenti |
| `.ino` | [hello.ino](variants/ext-ino-2e696e6f/hello.ino) creato, verifiche pendenti |
| `.ipp` | [hello.ipp](variants/ext-ipp-2e697070/hello.ipp) creato, verifiche pendenti |
| `.ixx` | [hello.ixx](variants/ext-ixx-2e697878/hello.ixx) creato, verifiche pendenti |
| `.re` | [hello.re](variants/ext-re-2e7265/hello.re) creato, verifiche pendenti |
| `.tcc` | [hello.tcc](variants/ext-tcc-2e746363/hello.tcc) creato, verifiche pendenti |
| `.tpp` | [hello.tpp](variants/ext-tpp-2e747070/hello.tpp) creato, verifiche pendenti |
| `.txx` | [hello.txx](variants/ext-txx-2e747878/hello.txx) creato, verifiche pendenti |
