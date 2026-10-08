# #435 MiniZinc Data

Caricare dati MiniZinc separati e usarli nel modello per costruire il saluto.

Tipo canonico `data`, language_id `938193433`.

Toolchain prevista: MiniZinc CLI e solver Gecode.

Dalla cartella dell’esempio:

```sh
minizinc --solver gecode model.mzn hello.dzn
```

Risultato atteso: dati accettati; soluzione con output Hello, World!.

hello.dzn è l’artefatto dati primario; model.mzn è il consumatore che verifica il valore caricato.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: MiniZinc 2.10.1 official Linux bundle + Gecode. [Log](verification/result.json). 

Fonti:

- [MiniZinc — data files](https://docs.minizinc.dev/en/stable/modelling.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dzn` | [hello.dzn](hello.dzn) verificato |
