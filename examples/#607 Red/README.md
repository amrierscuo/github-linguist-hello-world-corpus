# #607 Red

Voce canonica `Red`, tipo `programming`, language_id `320`.

Eseguire un programma Red con stringa composta e print.

## Toolchain e riproduzione

Required genuine red compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede la distribuzione Red ufficiale con console/runtime compatibile.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
red hello.red
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente Red originale; toolchain non configurata. Red e Rebol sono verificati separatamente.

Requisiti residui:

- Required red compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.red-lang.org/p/documentation.html](https://www.red-lang.org/p/documentation.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.red` | [hello.red](hello.red) creato, verifiche pendenti |
| `.reds` | [hello.reds](variants/reds-e7c6c4d7/hello.reds) creato, verifiche pendenti |
