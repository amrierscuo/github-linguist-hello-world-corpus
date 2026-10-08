# #326 JSON5

Analizzare JSON5 con chiave non quotata, stringa con apici e virgola finale.

Tipo canonico `data`, language_id `175`.

Toolchain prevista: Python 3.13 e libreria json5.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: Hello, World! e LF; oggetto con greeting corretto.

L’artefatto usa caratteristiche JSON5 effettive.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + json5 0.16.0. [Log](verification/result.json). 

Fonti:

- [JSON5 — specifica](https://spec.json5.org/)
- [pyjson5 — implementazione](https://github.com/dpranke/pyjson5)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install json5==0.16.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.json5` | [hello.json5](hello.json5) verificato |
