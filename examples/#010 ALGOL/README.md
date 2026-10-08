# #010 ALGOL

`hello.alg` è un programma ALGOL 60 per il dialetto e l'ambiente di I/O
**jff-algol**, che usa `outstring` e `newline` sul canale 1. Il risultato
atteso è una riga `Hello, World!`. La voce canonica usa `source.algol60`;
per questo l'esempio adotta ALGOL 60 e dichiara esplicitamente l'ambiente di I/O.

## Toolchain e comandi

Servono jff-algol di Jan van Katwijk, il suo preludio e runtime, e un compilatore
C nel suo ambiente Linux o Cygwin. Dalla cartella dell'esempio:

```sh
jff-algol hello.alg
./hello
```

Il driver traduce `hello.alg` in C, compila e collega l'eseguibile `hello`.
Per eseguire soltanto la traduzione front-end: `jff-algol -o hello.alg`.
Seguire il manuale per configurare jff-algol e i percorsi del runtime.

## Stato

Creato; sintassi e semantica **non verificate**. Non sono presenti jff-algol né
la sua toolchain C/Cygwin nel PATH dell'ambiente. Il programma è costruito secondo
la sintassi e le procedure documentate dall'autore; questa revisione delle fonti
non sostituisce la compilazione. Vedere `verification.log`.

## Fonte primaria

- [Manuale dell'autore di jff-algol, conservato nell'archivio ALGOL](https://gtoal.com/languages/algol60/jff-algol-60-compiler/doc/jff-manual.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.alg` | [hello.alg](hello.alg) creato, verifiche pendenti |
