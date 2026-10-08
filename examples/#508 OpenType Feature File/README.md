# #508 OpenType Feature File

Compilare una dichiarazione OpenType Feature File nella tabella name di un font.

Tipo canonico `data`, language_id `374317347`.

Toolchain prevista: Python e fontTools feaLib.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: name ID 4 costruito dal compiler e uguale al saluto.

Il saluto è il full font name; il fixture non pretende un font con glifi disegnati.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + fontTools 4.66.1 feaLib. [Log](verification/result.json). 

Fonti:

- [fontTools feaLib](https://fonttools.readthedocs.io/en/latest/feaLib/index.html)
- [Adobe feature file specification](https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install fonttools
```

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install fonttools==4.66.1
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fea` | [hello.fea](hello.fea) verificato |
