# 0749 — Verilog — `.veo`

Template di istanziazione Verilog da includere nel chiamante.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.veo`.

Controllo previsto, dalla cartella della variante:

```text
iverilog -I . -s main -o work/hello.vvp main.v hello.v; vvp work/hello.vvp
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Instantiating-Verilog-Modules](https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Instantiating-Verilog-Modules)
