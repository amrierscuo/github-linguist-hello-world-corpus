# #306 ISPC

Compilare una funzione ISPC esportata che stampa il saluto e invocarla da un harness C++.

## Toolchain

Intel(r) Implicit SPMD Program Compiler (Intel(r) ISPC), 1.31.0 (build commit c6adb4f86f5678ce @ 20260625, LLVM 23.0.0); g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Comandi e procedura

ispc hello.ispc --pic --target=sse2-i32x4 -h build/hello_ispc.h -o build/hello.o; g++ -I build main.cpp build/hello.o -o build/hello; build/hello

## Risultato atteso

Exit 0 e una riga Hello, World!.

## Stato

Sintassi e semantica verificate.

ISPC print è un’operazione di output originale; il saluto costante viene emesso una volta per gang. main.cpp è solo il chiamante dell’API generata. --pic consente il linking PIE del compilatore Ubuntu.

Verifica effettiva del 2026-10-08T12:31:12.168007+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://ispc.github.io/ispc.html](https://ispc.github.io/ispc.html)
- [https://github.com/ispc/ispc/releases/tag/v1.31.0](https://github.com/ispc/ispc/releases/tag/v1.31.0)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ispc` | [hello.ispc](hello.ispc) verificato |
