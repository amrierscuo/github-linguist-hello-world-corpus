# #452 Mustache

Voce canonica `Mustache`, tipo `markup`, language_id `638334590`.

Renderizzare un template Mustache parametrico e controllare l’escaping HTML.

## Toolchain e riproduzione

Existing Pystache Mustache compiler/renderer — 0.6.8. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python e Pystache 0.6.8; installazione isolata sotto work.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py hello.mustache
```

Risultato atteso: Hello, World! e PASS dei controlli del motore.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il renderer vero produce il saluto e la variante <Reader> è escapata come previsto; missing_tags strict.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://mustache.github.io/mustache.5.html](https://mustache.github.io/mustache.5.html)
- [https://pypi.org/project/pystache/](https://pypi.org/project/pystache/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mustache` | [hello.mustache](hello.mustache) verificato |
