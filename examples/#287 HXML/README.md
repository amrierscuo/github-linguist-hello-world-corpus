# #287 HXML

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Usare HXML per configurare il compiler Haxe ed eseguire il programma Hello, World!.

Il file HXML è l’artefatto principale: imposta classpath, classe main e backend --interp. Hello.hx è la fixture compilata. Il compiler Haxe reale legge la configurazione ed esegue il programma tramite il suo eval interpreter.

## Toolchain e riproduzione

Haxe4.3.3, pacchetto Ubuntu4.3.3-1build2

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
haxe hello.hxml
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://haxe.org/manual/compiler-usage-hxml.html
- https://haxe.org/manual/compiler-usage.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hxml` | [hello.hxml](hello.hxml) verificato |
