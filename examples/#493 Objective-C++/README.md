# #493 Objective-C++

Compilare una classe e inviare un messaggio Objective-C++.

## Toolchain

g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0; GNU libobjc4 14.2.0

## Procedura

g++ hello.mm -lobjc -o build/hello; build/hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

La classe usa Object del runtime GNU e un metodo di classe; Objective-C++ usa realmente anche std::string/std::cout. Nessuna libreria Foundation necessaria.

Verifica reale 2026-10-08T13:11:33.760305+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html](https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mm` | [hello.mm](hello.mm) verificato |
