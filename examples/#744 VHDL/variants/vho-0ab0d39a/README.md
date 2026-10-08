# 0744 — VHDL — `.vho`

Netlist VHDL strutturale scritta a mano con wire/constant cell originali; non dichiarata come export Quartus.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.vho`.

Controllo previsto, dalla cartella della variante:

```text
ghdl: analyze hello.vho and testbench.vhdl in work, elaborate/test greeting_tb
```

Risultato atteso: report note Hello, World! dopo assertion sul signal.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://ghdl.github.io/ghdl/using/InvokingGHDL.html](https://ghdl.github.io/ghdl/using/InvokingGHDL.html)
