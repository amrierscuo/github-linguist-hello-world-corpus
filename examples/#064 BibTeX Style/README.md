# #064 BibTeX Style

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Eseguire uno stile BibTeX originale che scrive il titolo Hello, World! nel file .bbl.

hello.bst è un programma nel linguaggio a stack di BibTeX: ENTRY, READ, ITERATE, write$ e newline$. input.bib e driver.aux sono fixture. L’avviso nativo sul tipo misc non definito è registrato: ITERATE applica direttamente write.greeting e non usa dispatch per tipo di voce.

## Toolchain e riproduzione

BibTeX 0.99e; MiKTeX-BibTeX 4.2 (MiKTeX 25.12)

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bibtex driver
```

## Risultato atteso e stato

driver.bbl esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://ctan.org/pkg/bibtex
- https://mirrors.ctan.org/biblio/bibtex/base/btxhak.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bst` | [hello.bst](hello.bst) verificato |
