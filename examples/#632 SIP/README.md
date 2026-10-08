# #632 SIP

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Generare binding Python per una funzione C che restituisce Hello, World!.

SIP è il linguaggio di descrizione dei binding C/C++ della voce .sip. Il parser e il generatore autentico producono wrapper C; nessuna estensione compilata è inclusa nel corpus.

## Toolchain e riproduzione

SIP6.17.0 originale, Python3.13

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python -m sipbuild.tools.build --no-compile --build-dir build
```

## Risultato atteso e stato

Parser accetta hello.sip e genera i binding corpus_greeting.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Compilazione e import dell’estensione C non eseguiti; restituzione del valore a runtime pendente.

## Fonti primarie

- https://python-sip.readthedocs.io/en/latest/directives.html#directive-Module

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sip` | [hello.sip](hello.sip) sintassi verificata |
