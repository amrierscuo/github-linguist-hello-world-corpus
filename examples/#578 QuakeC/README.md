# #578 QuakeC

Compilare QuakeC e invocare worldspawn in una VM compatibile.

## Toolchain

FTEQCC package 3343+svn3400-4; compiler version in stdout

## Procedura

fteqcc; caricare progs.dat in una VM Quake compatibile e chiamare worldspawn.

## Risultato atteso

Compilazione senza errori; worldspawn emette Hello, World! nel runtime Quake.

## Stato

Sintassi verificata; semantica in attesa.

Builtin #23 è bprint della VM Quake; il compilatore reale può verificare il bytecode, ma non si simula il builtin.

Verifica reale 2026-10-08T13:16:51.441635+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- Quake VM fixture not available; native execution pending.

## Fonti primarie

- [https://github.com/fte-team/fteqw](https://github.com/fte-team/fteqw)
- [https://github.com/id-Software/Quake/blob/master/WinQuake/pr_cmds.c](https://github.com/id-Software/Quake/blob/master/WinQuake/pr_cmds.c)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.qc` | [hello.qc](hello.qc) sintassi verificata |
