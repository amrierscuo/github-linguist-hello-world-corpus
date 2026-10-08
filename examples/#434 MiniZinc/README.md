# #434 MiniZinc

Risolvere un modello MiniZinc senza vincoli e produrre il saluto nell’output.

Tipo canonico `programming`, language_id `238874535`.

Toolchain prevista: MiniZinc CLI e solver Gecode.

Dalla cartella dell’esempio:

```sh
minizinc --solver gecode hello.mzn
```

Risultato atteso: soluzione soddisfacibile con riga Hello, World! nell’output.

Il solve item e output item sono interpretati dal compilatore MiniZinc reale.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: MiniZinc 2.10.1 official Linux bundle + Gecode. [Log](verification/result.json). 

Fonti:

- [MiniZinc — manuale](https://docs.minizinc.dev/en/stable/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mzn` | [hello.mzn](hello.mzn) verificato |
