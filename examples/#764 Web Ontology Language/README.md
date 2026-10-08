# #764 Web Ontology Language

Voce canonica `Web Ontology Language`, tipo `data`, language_id `394`.

Ontologia OWL originale serializzata in RDF/XML, con una classe Greeting e l’etichetta inglese `Hello, World!`.

## Toolchain e riproduzione

rdflib / Python 3.13.9 — 7.6.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e RDFLib 7.6.0 in ambiente isolato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! e PASS per classe e label nel grafo RDF.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

RDFLib legge la serializzazione e le asserzioni controllano i triple OWL.Class e rdfs:label con language tag en. Non viene attestata la consistenza di un’ontologia mediante un reasoner: l’obiettivo è questo piccolo grafo e la sua etichetta.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.w3.org/TR/owl2-primer/](https://www.w3.org/TR/owl2-primer/)
- [https://rdflib.readthedocs.io/en/stable/](https://rdflib.readthedocs.io/en/stable/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.owl` | [hello.owl](hello.owl) verificato |
