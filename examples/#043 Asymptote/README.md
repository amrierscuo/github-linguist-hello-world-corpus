# #043 Asymptote

Voce canonica: `Asymptote`, tipo `programming`, `language_id: 591605007`.

Concatenare Hello, e World! e scrivere il saluto su stdout Asymptote.

## Toolchain e riproduzione

Asymptote interpreter distributed with MiKTeX — miktex-asy version 2.88 [(C) 2004 Andy Hammerlindl, John C. Bowman, Tom Prince]. Ambiente della prova: **Windows x64**.

Richiede Asymptote e una distribuzione coerente dei suoi moduli standard. Non usa grafica, TeX o un viewer: il programma invoca solo write su una stringa.

Comando/procedura dalla directory dell’esempio:

```text
asy -noV hello.asy
```

Risultato atteso: Exit 0; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

L’interprete MiKTeX locale è stato eseguito davvero, ma non carica il modulo plain: il log mostra errori sui moduli standard prima dell’esecuzione del sorgente. Occorre una toolchain coerente; sintassi e semantica restano false.

Requisiti residui:

- Asymptote interpreter runs, but local MiKTeX standard plain modules produce compiler errors; coherent interpreter/library installation required.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://asymptote.sourceforge.io/doc/Files.html](https://asymptote.sourceforge.io/doc/Files.html)
- [https://asymptote.sourceforge.io/doc/Options.html](https://asymptote.sourceforge.io/doc/Options.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asy` | [hello.asy](hello.asy) creato, verifiche pendenti |
