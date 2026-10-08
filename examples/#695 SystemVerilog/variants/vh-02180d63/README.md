# 0695 — SystemVerilog — `.vh`

Header SystemVerilog con macro e guard.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.vh`.

Controllo previsto, dalla cartella della variante:

```text
iverilog -g2012 -I . -o work/hello.vvp main.sv; vvp work/hello.vvp
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://steveicarus.github.io/iverilog/usage/command_line_flags.html](https://steveicarus.github.io/iverilog/usage/command_line_flags.html)
