# #744 VHDL

Simulare VHDL e produrre una report note con il saluto.

Tipo canonico `programming`, language_id `385`.

Toolchain prevista: GHDL 4.1.0 (Ubuntu 4.1.0+dfsg-0ubuntu2.1) [Dunoon edition]; mcode JIT backend; GNAT13.3.0; WSL Ubuntu24.04.

Dalla cartella dell’esempio:

```sh
mkdir -p build
ghdl -a --std=08 --workdir=build hello.vhdl
ghdl -e --std=08 --workdir=build hello
ghdl -r --std=08 --workdir=build hello --stop-time=1ns
```

Risultato atteso: analisi/elaborazione riuscita; report note Hello, World!.

La stringa compare nel report del simulatore; non è una console UART hardware.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: GHDL 4.1.0 (Ubuntu 4.1.0+dfsg-0ubuntu2.1) [Dunoon edition]; mcode JIT backend; GNAT13.3.0; WSL Ubuntu24.04. [Log](verification/result.json). 

Fonti:

- [GHDL simulation](https://ghdl.github.io/ghdl/using/InvokingGHDL.html)

La verifica reale usa pacchetti Ubuntu originali estratti sotto `work/tools_741_760/ubuntu` e directory di build separate sotto `work/tools_741_760`; gli artefatti compilati non fanno parte del corpus. I comandi e gli environment effettivi sono nel log.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vhdl` | [hello.vhdl](hello.vhdl), [greeting.vhdl](variants/vhi-77848f30/greeting.vhdl), [main.vhdl](variants/vhi-77848f30/main.vhdl), [testbench.vhdl](variants/vho-0ab0d39a/testbench.vhdl) creato, verifiche pendenti |
| `.vhd` | [hello.vhd](variants/vhd-b8ea5231/hello.vhd) creato, verifiche pendenti |
| `.vhf` | [hello.vhf](variants/vhf-90e3bf30/hello.vhf) creato, verifiche pendenti |
| `.vhi` | [hello.vhi](variants/vhi-77848f30/hello.vhi) creato, verifiche pendenti |
| `.vho` | [hello.vho](variants/vho-0ab0d39a/hello.vho) creato, verifiche pendenti |
| `.vhs` | [hello.vhs](variants/vhs-dc5efabf/hello.vhs) creato, verifiche pendenti |
| `.vht` | [hello.vht](variants/vht-b9b9d435/hello.vht) creato, verifiche pendenti |
| `.vhw` | [hello.vhw](variants/vhw-27e673c9/hello.vhw) creato, verifiche pendenti |
