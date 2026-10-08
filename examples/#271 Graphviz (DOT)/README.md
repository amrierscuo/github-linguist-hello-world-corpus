# #271 Graphviz (DOT)

Voce canonica `Graphviz (DOT)`, tipo `data`, language_id `140`.

Renderizzare un nodo DOT con l’etichetta Hello, World! in un SVG prodotto da Graphviz.

## Toolchain e riproduzione

Genuine Graphviz DOT parser and SVG layout renderer — dot - graphviz version 2.43.0 (0). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Graphviz 2.43.0 disponibile su Ubuntu WSL2. Il prodotto SVG rimane in build. verify_svg.py legge l’XML del prodotto reale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
dot -Tsvg hello.dot -o build/hello.svg; python verify_svg.py build/hello.svg
```

Risultato atteso: SVG valido con testo Hello, World!; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Graphviz fa parsing e layout autentici. La verifica semantica conferma la presenza del saluto nel nodo text dell’SVG prodotto; il log registra il suo hash.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.graphviz.org/doc/info/lang.html](https://www.graphviz.org/doc/info/lang.html)
- [https://graphviz.org/docs/outputs/svg/](https://graphviz.org/docs/outputs/svg/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dot` | [hello.dot](hello.dot) verificato |
| `.gv` | [hello.gv](variants/ext-gv-2e6776/hello.gv) creato, verifiche pendenti |
