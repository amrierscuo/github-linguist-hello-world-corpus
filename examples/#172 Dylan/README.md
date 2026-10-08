# #172 Dylan

Compilare una libreria eseguibile Dylan e scrivere Hello, World! con format-out.

## Toolchain

Open Dylan con librerie common-dylan/io; versione concreta da registrare

## Comandi e procedura

dylan-compiler -build hello.lid; _build/bin/hello

## Risultato atteso

Compilazione e linking exit 0; eseguibile stampa il saluto più newline.

## Stato

Sintassi e semantica in attesa.

library.dylan dichiara library e module, hello.lid elenca prima la dichiarazione e poi il programma. Il programma usa il formato console del modulo format-out. Non è stata sostituita la toolchain Dylan con un parser generico.

Requisiti residui:
- Toolchain Open Dylan e librerie non predisposte; compilazione/linking/esecuzione pending.

## Fonti primarie e riferimento di formato

- [https://opendylan.org/getting-started-cli/hello-world.html](https://opendylan.org/getting-started-cli/hello-world.html)
- [https://opendylan.org/library-reference/io/format-out.html](https://opendylan.org/library-reference/io/format-out.html)
- [https://opendylan.org/download/index.html](https://opendylan.org/download/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dylan` | [hello.dylan](hello.dylan), [library.dylan](library.dylan) creato, verifiche pendenti |
| `.dyl` | [hello.dyl](variants/ext-dyl-2e64796c/hello.dyl) creato, verifiche pendenti |
| `.intr` | [hello.intr](variants/ext-intr-2e696e7472/hello.intr) creato, verifiche pendenti |
| `.lid` | [hello.lid](hello.lid) creato, verifiche pendenti |
