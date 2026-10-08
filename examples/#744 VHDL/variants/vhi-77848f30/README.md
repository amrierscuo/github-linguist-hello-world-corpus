# 0744 — VHDL — `.vhi`

Template di istanziazione VHDL da inserire nell’architecture; non unità VHDL autonoma.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.vhi`.

Controllo previsto, dalla cartella della variante:

```text
ghdl: analyze greeting.vhdl and expanded main.vhdl; simulate main
```

Risultato atteso: signal message assume Hello, World! e report note del chiamante.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Using-VHDL-Instantiation-Templates](https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Using-VHDL-Instantiation-Templates)
