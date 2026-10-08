# #795 Xtend

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare Xtend e stampare Hello, World!.

Programma Xtend originale con val e println. Un compilatore Java applicato direttamente al file non verifica Xtend.

## Toolchain e riproduzione

Eclipse Xtend compiler/Xbase, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Eclipse Xtend: compilare Hello.xtend nel progetto Java di prova e avviare Hello.main
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compiler Xtend/Xbase non predisposto; generazione Java ed esecuzione pendenti.

## Fonti primarie

- https://eclipse.dev/xtend/documentation/102_basics.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xtend` | [Hello.xtend](Hello.xtend) creato, verifiche pendenti |
