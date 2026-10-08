# #053 BASIC

Voce canonica `BASIC`, tipo `programming`, language_id `28923963`.

Stampare Hello, World! in un programma BASIC scegliendo il dialetto Yabasic.

## Toolchain e riproduzione

Yabasic Ubuntu binary package extracted locally yabasic 2.90.3, built on x86_64-pc-linux-gnu.

Comando dalla directory del campione con Yabasic 2.90.3. I numeri di linea sono accettati da questa toolchain; la prova registra il suo stdout esatto.

```text
yabasic hello.bas
```

Risultato atteso: Exit 0, stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Programma Yabasic con numeri di linea 10 e 20; il runtime originale li accetta e stampa esattamente il saluto. La numerazione esplicita rende riconoscibile il campione BASIC secondo la regola upstream .bas. La prova riguarda il dialetto Yabasic, non tutti i BASIC storici.

Prova corrente: [recognition.json](verification/recognition.json), con UTC, comandi nativi, exit code, stdout/stderr, toolchain e SHA-256 dei sorgenti modificati e dei driver. Le prove precedenti restano come storico. L’identificazione prevista da Linguist è distinta dall’esito effettivo delle statistiche GitHub; questo lotto non applica override di linguaggio.

## Fonti primarie

- https://www.yabasic.de/yabasic.htm
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.bas` | [hello.bas](hello.bas) sintassi e semantica verificate |
