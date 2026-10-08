# #327 JSONLD

Espandere JSON-LD e associare Hello, World! all’IRI greeting del contesto locale.

Tipo canonico `data`, language_id `176`.

Toolchain prevista: Python 3.13 e PyLD.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: valore RDF espanso Hello, World! con IRI previsto; stdout saluto e LF.

Il contesto è incorporato: non servono richieste di rete. example.invalid è usato soltanto come identificatore.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + PyLD 3.3.0. [Log](verification/result.json). 

Fonti:

- [W3C — JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)
- [Digital Bazaar — PyLD](https://github.com/digitalbazaar/pyld)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install pyld==3.3.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jsonld` | [hello.jsonld](hello.jsonld) verificato |
