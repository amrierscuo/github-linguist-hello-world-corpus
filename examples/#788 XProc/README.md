# #788 XProc

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire una pipeline XProc3 che produce un documento greeting.

La pipeline identity usa un input inline originale e porta result. Un parser XML generico non verifica il linguaggio di pipeline.

## Toolchain e riproduzione

Processore XProc3 come XML Calabash3, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
xmlcalabash hello.xpl
```

## Risultato atteso e stato

Documento <greeting>Hello, World!</greeting>.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Processore XProc3 non predisposto; validazione e pipeline pendenti.

## Fonti primarie

- https://spec.xproc.org/3.0/xproc/xproc_letter.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xpl` | [hello.xpl](hello.xpl) creato, verifiche pendenti |
| `.xproc` | [hello.xproc](variants/xproc-8b475bd1/hello.xproc) creato, verifiche pendenti |
