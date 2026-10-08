# 0765 — WebAssembly — `.wast`

WebAssembly spec test script con module e assertion, non solo WAT rinominato.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.wast`.

Controllo previsto, dalla cartella della variante:

```text
wast2json hello.wast -o work/hello.json; spectest-interp work/hello.json
```

Risultato atteso: assert_return passano; il modulo conserva il saluto in memoria.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://github.com/WebAssembly/wabt](https://github.com/WebAssembly/wabt)
- [https://github.com/WebAssembly/spec/tree/main/interpreter](https://github.com/WebAssembly/spec/tree/main/interpreter)
