# #749 Verilog

Simulare un modulo Verilog che esegue display e finish.

Tipo canonico `programming`, language_id `387`.

Toolchain prevista: Icarus Verilog12.0 native Linux compiler/vvp.

Dalla cartella dell’esempio:

```sh
iverilog -o build/hello.vvp hello.v
vvp build/hello.vvp
```

Risultato atteso: La simulazione stampa una riga Hello, World! e la diagnostica normale $finish called at 0; exit0.

Il programma non descrive un dispositivo esterno: è un testbench di simulazione.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Icarus Verilog12.0 original compiler/vvp native Linux. [Log](verification/result.json). 

Fonti:

- [Icarus Verilog](https://steveicarus.github.io/iverilog/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.v` | [hello.v](hello.v), [hello.v](variants/veo-6cbf9bdf/hello.v), [main.v](variants/veo-6cbf9bdf/main.v) creato, verifiche pendenti |
| `.veo` | [hello.veo](variants/veo-6cbf9bdf/hello.veo) creato, verifiche pendenti |
