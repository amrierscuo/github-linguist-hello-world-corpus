# 0744 — VHDL — `.vhw`

Variante testuale dello stesso formato, con suffisso canonico .vhw.

Provenienza: copia del file originale `examples/#744 VHDL/hello.vhdl`.

Artefatto principale: `hello.vhw`.

Controllo previsto, dalla cartella della variante:

```text
ghdl -a --std=08 --workdir=work hello.vhw
ghdl -e --std=08 --workdir=work hello
ghdl -r --std=08 --workdir=work hello --stop-time=1ns
```

Risultato atteso: analisi/elaborazione riuscita; report note Hello, World!..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://ghdl.github.io/ghdl/using/InvokingGHDL.html](https://ghdl.github.io/ghdl/using/InvokingGHDL.html)
