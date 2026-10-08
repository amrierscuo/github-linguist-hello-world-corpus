# #280 HTML

Voce canonica `HTML`, tipo `markup`, language_id `146`.

Analizzare un documento HTML5 valido e controllare il testo visibile di un heading h1 sotto main.

## Toolchain e riproduzione

Existing html5lib strict HTML5 tree builder — 1.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

html5lib 1.1 su Python 3.13.9. Il documento include doctype, lingua, charset e title. Il parser strict solleva errori su parsing non conforme.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python -m pip install html5lib==1.1; python verify.py hello.html
```

Risultato atteso: Zero errori parser; heading Hello, World!; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova delega tokenizzazione e costruzione del DOM al parser HTML5 esistente; controlla title, lingua e testo del heading. L’ambito semantico è il DOM con contenuto visibile, senza dichiarare un rendering visivo dei pixel.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/)
- [https://html5lib.readthedocs.io/en/latest/](https://html5lib.readthedocs.io/en/latest/)
- [https://github.com/html5lib/html5lib-python](https://github.com/html5lib/html5lib-python)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.html` | [hello.html](hello.html) verificato |
| `.hta` | [hello.hta](variants/ext-hta-2e687461/hello.hta) creato, verifiche pendenti |
| `.htm` | [hello.htm](variants/ext-htm-2e68746d/hello.htm) creato, verifiche pendenti |
| `.html.hl` | [hello.html.hl](variants/ext-html-hl-2e68746d6c2e686c/hello.html.hl) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) creato, verifiche pendenti |
| `.xht` | [hello.xht](variants/ext-xht-2e786874/hello.xht) creato, verifiche pendenti |
| `.xhtml` | [hello.xhtml](variants/ext-xhtml-2e7868746d6c/hello.xhtml) creato, verifiche pendenti |
