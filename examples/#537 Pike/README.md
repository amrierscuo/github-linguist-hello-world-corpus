# #537 Pike

Voce canonica `Pike`, tipo `programming`, language_id `287`.

Eseguire un main Pike che formatta e scrive il saluto.

## Toolchain e riproduzione

Genuine Pike language interpreter — Pike v8.0 release 1738 Copyright © 1994-2022 Linköping University; Pike comes with ABSOLUTELY NO WARRANTY; This is free software and you are; welcome to redistribute it under certain conditions; read the files; COPYING and COPYRIGHT in the Pike distribution for more details.. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pike 8.0 release 1738 autentico. La distribuzione relocata usa PIKE_MODULE_PATH, PIKE_INCLUDE_PATH e -m master.pike, tutti registrati nel log.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
pike hello.pike
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Runtime originale legge ed esegue il main; stdout esatto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pike.lysator.liu.se/docs/man/](https://pike.lysator.liu.se/docs/man/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pike` | [hello.pike](hello.pike), [driver.pike](variants/pmod-c6f9853d/driver.pike) creato, verifiche pendenti |
| `.pmod` | [hello.pmod](variants/pmod-c6f9853d/hello.pmod) creato, verifiche pendenti |
