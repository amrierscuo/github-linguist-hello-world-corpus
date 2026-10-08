# #049 B

Voce canonica: `B`, tipo `programming`, `language_id: 700792152`.

Emettere i caratteri ASCII di Hello, World! uno per volta tramite la libreria putchar del linguaggio storico B.

## Toolchain e riproduzione

b — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede una toolchain del B storico di Ken Thompson e la sua libreria putchar. Nessuna toolchain B è stata trovata; non viene compilato come C.

Comando/procedura dalla directory dell’esempio:

```text
Compilatore storico B: compilare hello.b con la libreria che espone putchar; eseguire il programma risultante (comando specifico da registrare quando disponibile).
```

Risultato atteso: Compilazione B riuscita; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

extrn dichiara la funzione esterna. La newline usa la convenzione B *n. Il programma evita assunzioni sulla disposizione packed delle stringhe B; le chiamate lavorano con singoli caratteri.

Requisiti residui:

- b toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://www.bell-labs.com/usr/dmr/www/btut.pdf](https://www.bell-labs.com/usr/dmr/www/btut.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.b` | [hello.b](hello.b) creato, verifiche pendenti |
