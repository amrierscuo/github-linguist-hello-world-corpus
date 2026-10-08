# #063 BibTeX

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Leggere una voce bibliografica il cui titolo è Hello, World! e generare la bibliografia.

hello.bib è il database BibTeX. driver.aux specifica citazione, database e stile standard plain. La semantica verificata è la generazione del titolo nel file .bbl, non una compilazione PDF LaTeX.

## Toolchain e riproduzione

BibTeX 0.99e; MiKTeX-BibTeX 4.2 (MiKTeX 25.12); plain.bst

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bibtex driver
```

## Risultato atteso e stato

driver.bbl contiene il titolo {Hello, World!}; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://ctan.org/pkg/bibtex
- https://mirrors.ctan.org/biblio/bibtex/base/btxdoc.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bib` | [hello.bib](hello.bib) verificato |
| `.bibtex` | [hello.bibtex](variants/ext-bibtex-2e626962746578/hello.bibtex) creato, verifiche pendenti |
