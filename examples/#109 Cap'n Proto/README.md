# #109 Cap'n Proto

Analizzare uno schema Cap’n Proto, creare Greeting con il valore predefinito e conservarlo in un ciclo serializzazione/lettura.

Tipo canonico: `programming`; `language_id`: `52`.

Toolchain prevista: Python 3 e pycapnp (binding del parser/runtime C++ Cap’n Proto). La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
python verify.py
```

Risultato atteso: default e round-trip entrambi uguali a `Hello, World!`; stampa del saluto e uscita 0.

L’identificativo dello schema è stato generato casualmente con il bit alto impostato. Il controllo usa il parser nativo tramite pycapnp, non un parser costruito per il corpus.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: Python 3.13.9 + pycapnp 2.2.4 (native Cap’n Proto parser/runtime). Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [Cap’n Proto — linguaggio degli schemi](https://capnproto.org/language.html)
- [pycapnp — lettura e scrittura](https://capnproto.github.io/pycapnp/quickstart.html)

Dipendenze riproducibili in una cartella di lavoro dedicata:

```sh
python -m pip install pycapnp==2.2.4
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.capnp` | [hello.capnp](hello.capnp) verificato |
