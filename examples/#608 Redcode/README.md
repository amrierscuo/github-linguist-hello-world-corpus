# #608 Redcode

Voce canonica `Redcode`, tipo `programming`, language_id `321`.

Caricare un warrior Redcode originale con i codici ASCII del saluto nel suo segmento dati.

## Toolchain e riproduzione

Required genuine pmars compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede pMARS ICWS-94 con CORESIZE 8000 e accesso alla vista memoria del simulatore.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
pmars -a hello.cw; pmars hello.cw hello.cw
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Redcode non possiede I/O stringa: il goal eÌ€ assemblare e osservare i 13 operand A delle DAT, che ricostruiscono Hello, World!, mentre JMP mantiene il processo. Parser/simulatore mancanti; nessun claim di output console.

Requisiti residui:

- Required pmars compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [http://www.koth.org/pmars/](http://www.koth.org/pmars/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cw` | [hello.cw](hello.cw) creato, verifiche pendenti |
