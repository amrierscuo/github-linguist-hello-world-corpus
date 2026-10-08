# #056 BQN

Voce canonica: `BQN`, tipo `programming`, `language_id: 330386870`.

Concatenare tre stringhe BQN e scrivere Hello, World! usando il sistema •Out.

## Toolchain e riproduzione

Official CBQN C implementation locally built — c893d3e7828899a50150df03ad33c9052fa51d3c. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

CBQN compilato dal repository ufficiale, commit c893d3e7828899a50150df03ad33c9052fa51d3c. Build locale Linux: make REPLXX=0 FFI=0 -j2. Le feature REPL editor e FFI non servono al programma.

Comando/procedura dalla directory dell’esempio:

```text
BQN hello.bqn
```

Risultato atteso: Exit 0; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La verifica usa il vero interprete CBQN. Il log contiene commit ed SHA-256 del binario, oltre al SHA-256 del sorgente BQN. La concatenazione ∾ e l’assegnazione ← sono sintassi BQN.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://mlochbaum.github.io/BQN/doc/quick.html](https://mlochbaum.github.io/BQN/doc/quick.html)
- [https://github.com/dzaima/CBQN](https://github.com/dzaima/CBQN)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bqn` | [hello.bqn](hello.bqn) verificato |
