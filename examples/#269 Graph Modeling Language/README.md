# #269 Graph Modeling Language

Voce canonica `Graph Modeling Language`, tipo `data`, language_id `138`.

Rappresentare un grafo diretto GML con un nodo etichettato dal saluto.

## Toolchain e riproduzione

NetworkX native GML reader — 3.5. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

NetworkX 3.5 su Python 3.13.9. read_gml(label=None) conserva l’id numerico e legge label come attributo.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python -m pip install networkx==3.5; python verify.py hello.gml
```

Risultato atteso: Hello, World! e PASS dei campi del grafo.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il reader esistente analizza il formato e il controllo verifica un solo nodo 0, grafo diretto, zero archi e label esatta. Nessun parser GML fatto in casa è usato.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.gml.read_gml.html](https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.gml.read_gml.html)
- [https://github.com/networkx/networkx](https://github.com/networkx/networkx)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gml` | [hello.gml](hello.gml) verificato |
