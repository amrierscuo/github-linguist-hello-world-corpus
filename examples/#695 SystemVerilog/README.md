# #695 SystemVerilog

Voce canonica `SystemVerilog`, tipo `programming`, language_id `363`.

Compilare e simulare un testbench SystemVerilog2012 che stampa il saluto.

## Toolchain e riproduzione

Authentic Icarus SystemVerilog compiler and vvp simulator — Icarus 12.0-2build2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Icarus Verilog12.0 autentico, frontend selezionato con -g2012; tool relocato usa -B per le componenti native.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
iverilog -g2012 -o build/hello.vvp hello.sv; vvp build/hello.vvp
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Compiler e simulator genuini eseguono string, display e finish; prima riga stdout esatta.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://steveicarus.github.io/iverilog/usage/command_line_flags.html](https://steveicarus.github.io/iverilog/usage/command_line_flags.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sv` | [hello.sv](hello.sv), [main.sv](variants/svh-80e139de/main.sv), [main.sv](variants/vh-02180d63/main.sv) creato, verifiche pendenti |
| `.svh` | [hello.svh](variants/svh-80e139de/hello.svh) creato, verifiche pendenti |
| `.vh` | [hello.vh](variants/vh-02180d63/hello.vh) creato, verifiche pendenti |
