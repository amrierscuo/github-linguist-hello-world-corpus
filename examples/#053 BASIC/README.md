# #053 BASIC

Voce canonica: `BASIC`, tipo `programming`, `language_id: 28923963`.

Stampare Hello, World! in un programma BASIC scegliendo il dialetto Yabasic.

## Toolchain e riproduzione

Yabasic Ubuntu binary package extracted locally — yabasic 2.90.3, built on x86_64-pc-linux-gnu. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Toolchain scelta: Yabasic 2.90.3, pacchetto Ubuntu estratto con le sue dipendenze in work. Il programma usa print e end del dialetto Yabasic.

Comando/procedura dalla directory dell’esempio:

```text
yabasic hello.bas
```

Risultato atteso: Exit 0; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La verifica autentica conta soltanto questo dialetto della voce BASIC. Non attesta la compatibilità con tutti i BASIC storici.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://www.yabasic.de/yabasic.htm](https://www.yabasic.de/yabasic.htm)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bas` | [hello.bas](hello.bas) verificato |
