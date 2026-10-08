# #644 SWIG

Generare un binding SWIG C/Python e invocare greeting.

## Toolchain

SWIG Version 4.1.0

Compiled with g++ [x86_64-pc-linux-gnu]

Configured options: +pcre

Please see https://www.swig.org for reporting bugs and further information; Python 3.12.3; GCC13.3.0

## Procedura

swig -python -outdir build -o build/hello_wrap.c hello.i; gcc -shared -fPIC -I<python3.12-headers> build/hello_wrap.c -o build/_hello.so; PYTHONPATH=build python3 verify.py

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:23:07.256159+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://swig.org/Doc4.3/SWIGDocumentation.html](https://swig.org/Doc4.3/SWIGDocumentation.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.i` | [hello.i](hello.i) verificato |
| `.swg` | [hello.swg](variants/swg-a3424d42/hello.swg) creato, verifiche pendenti |
| `.swig` | [hello.swig](variants/swig-b750f324/hello.swig) creato, verifiche pendenti |
