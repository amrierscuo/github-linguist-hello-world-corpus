# #485 OCaml

Compilare ed eseguire OCaml.

## Toolchain

OCaml 4.14.1

## Procedura

ocamlc -o build/hello hello.ml; ocamlrun build/hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:10:44.031687+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://ocaml.org/manual/5.4/programs.html](https://ocaml.org/manual/5.4/programs.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ml` | [hello.ml](hello.ml), [greeting.ml](variants/mli-2a1ba63b/greeting.ml), [main.ml](variants/mli-2a1ba63b/main.ml), [driver.ml](variants/mly-4acf893e/driver.ml) creato, verifiche pendenti |
| `.eliom` | [hello.eliom](variants/eliom-eb7291f2/hello.eliom) creato, verifiche pendenti |
| `.eliomi` | [greeting.eliomi](variants/eliomi-438ad78e/greeting.eliomi) creato, verifiche pendenti |
| `.ml4` | [hello.ml4](variants/ml4-65957964/hello.ml4) creato, verifiche pendenti |
| `.mli` | [greeting.mli](variants/mli-2a1ba63b/greeting.mli) creato, verifiche pendenti |
| `.mll` | [hello.mll](variants/mll-85b0301a/hello.mll) creato, verifiche pendenti |
| `.mly` | [hello.mly](variants/mly-4acf893e/hello.mly) creato, verifiche pendenti |
