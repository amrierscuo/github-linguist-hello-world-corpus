# 0633 — SMT — `.z3`

Variante testuale dello stesso formato, con suffisso canonico .z3.

Provenienza: copia del file originale `examples/#633 SMT/hello.smt2`.

Artefatto principale: `hello.z3`.

Controllo previsto, dalla cartella della variante:

```text
z3 -smt2 hello.z3
```

Risultato atteso: sat e ((greeting "Hello, World!"))..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://smt-lib.org/theories-UnicodeStrings.shtml](https://smt-lib.org/theories-UnicodeStrings.shtml)
