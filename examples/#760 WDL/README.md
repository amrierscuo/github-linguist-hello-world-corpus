# #760 WDL

Analizzare/typecheck un workflow WDL che produce e legge un file stdout di saluto.

Tipo canonico `programming`, language_id `374521672`.

Toolchain prevista: miniwdl1.15.0 original parser/typechecker on Python3.12 Linux; task backend pending.

Dalla cartella dell’esempio:

```sh
python verify.py
miniwdl run hello.wdl
```

Risultato atteso: workflow valido; task output message Hello, World!.

Parsing/typecheck è distinto dall’esecuzione del task.

Stato registrato: sintassi verificata; semantica in attesa. Toolchain: miniwdl original parser/typechecker on Python3.12 Linux. [Log](verification/result.json). Parsing e typecheck WDL reali passano su Linux; backend task non eseguito.

Fonti:

- [WDL specification](https://github.com/openwdl/wdl/blob/wdl-1.0/SPEC.md)
- [miniwdl](https://github.com/chanzuckerberg/miniwdl)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install miniwdl
```

miniwdl usa librerie POSIX: il controllo reale è stato eseguito su Linux. Il test non avvia il backend dei task.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.wdl` | [hello.wdl](hello.wdl) sintassi verificata |
