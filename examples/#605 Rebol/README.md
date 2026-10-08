# #605 Rebol

Voce canonica `Rebol`, tipo `programming`, language_id `319`.

Eseguire un programma Rebol con rejoin e print.

## Toolchain e riproduzione

Original Rebol3 Oldes branch interpreter — Rebol/Bulk 3.22.1 (2026-05-27 19:59:00 UTC); Copyright (c) 2012 REBOL Technologies; Copyright (c) 2012-2026 Rebol Open Source Contributors; Source:       https://github.com/Oldes/Rebol3. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Rebol/Bulk 3.22.1 Oldes branch, originale release Linux x64. SHA dell’asset corrisponde alla release primaria.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
rebol3 -q hello.reb
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Interpreter genuino, script originale e stdout esatto. Il binario Windows non funziona nel terminale non interattivo di prova, quindi eÌ€ usato il runtime Linux ufficiale.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/Oldes/Rebol3](https://github.com/Oldes/Rebol3)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.reb` | [hello.reb](hello.reb) verificato |
| `.r` | [hello.r](variants/r-8dbb84b2/hello.r) creato, verifiche pendenti |
| `.r2` | [hello.r2](variants/r2-8d1288b8/hello.r2) creato, verifiche pendenti |
| `.r3` | [hello.r3](variants/r3-172ccdf0/hello.r3) creato, verifiche pendenti |
| `.rebol` | [hello.rebol](variants/rebol-747e1472/hello.rebol) creato, verifiche pendenti |
