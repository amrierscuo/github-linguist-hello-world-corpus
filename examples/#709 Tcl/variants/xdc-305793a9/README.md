# 0709 — Tcl — `.xdc`

Constraint Tcl per timing Xilinx XDC; richiede un design con port clk.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.xdc`.

Controllo previsto, dalla cartella della variante:

```text
native FPGA/STA tool: load RTL main.v and read XDC hello.xdc
```

Risultato atteso: clock corpus_greeting con periodo 10 ns; RTL di simulazione produce Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.amd.com/r/en-US/ug903-vivado-using-constraints/Clock-Definition](https://docs.amd.com/r/en-US/ug903-vivado-using-constraints/Clock-Definition)
