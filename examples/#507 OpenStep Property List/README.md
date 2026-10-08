# #507 OpenStep Property List

Analizzare una property list OpenStep ASCII e leggere greeting.

Tipo canonico `data`, language_id `598917541`.

Toolchain prevista: Python e openstep-parser.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: dizionario con valore Hello, World!.

Il formato con parentesi graffe e punto e virgola è distinto da XML e binary plist.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + openstep-parser 2.0.3. [Log](verification/result.json). 

Fonti:

- [OpenStep parser](https://github.com/kronenthaler/openstep-parser)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install openstep-parser==2.0.3
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.plist` | [hello.plist](hello.plist) verificato |
| `.glyphs` | [hello.glyphs](variants/glyphs-cb9da07f/hello.glyphs) creato, verifiche pendenti |
