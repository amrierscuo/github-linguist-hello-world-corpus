# #613 RenderScript

Voce canonica `RenderScript`, tipo `programming`, language_id `323`.

Scrivere il saluto tramite rsDebug in un kernel/script Android RenderScript.

## Toolchain e riproduzione

Required genuine llvm-rs-cc compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede toolchain storica Android RenderScript e rs_debug.rsh, Java package org.corpus.greeting.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
llvm-rs-cc -I /path/to/renderscript/include -o build hello.rs; caricare il relativo ScriptC_hello ed eseguire invoke_hello in un progetto Android compatibile.
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale con pragma version/java package e funzione hello. Toolchain storica e Android runtime non configurati.

Requisiti residui:

- Required llvm-rs-cc compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://developer.android.com/guide/topics/renderscript/reference/rs_debug](https://developer.android.com/guide/topics/renderscript/reference/rs_debug)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rs` | [hello.rs](hello.rs), [main.rs](variants/rsh-e00ceaaf/main.rs) creato, verifiche pendenti |
| `.rsh` | [hello.rsh](variants/rsh-e00ceaaf/hello.rsh) creato, verifiche pendenti |
