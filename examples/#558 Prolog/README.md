# #558 Prolog

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare Prolog e risolvere main che stampa Hello, World!.

initialization(main,main) definisce l’avvio del programma. atomic_list_concat costruisce il valore e writeln lo emette nel runtime Prolog originale.

## Toolchain e riproduzione

SWI-Prolog9.0.4 ufficiale Ubuntu

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
swipl -q hello.pl
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.swi-prolog.org/pldoc/doc_for?object=atomic_list_concat/2
- https://www.swi-prolog.org/pldoc/doc_for?object=initialization/2

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pl` | [hello.pl](hello.pl) verificato |
| `.plt` | [hello.plt](variants/plt-cc71c907/hello.plt) creato, verifiche pendenti |
| `.pro` | [hello.pro](variants/pro-1d8a87ac/hello.pro) creato, verifiche pendenti |
| `.prolog` | [hello.prolog](variants/prolog-26531ed3/hello.prolog) creato, verifiche pendenti |
| `.yap` | [hello.yap](variants/yap-42bad85d/hello.yap) creato, verifiche pendenti |
