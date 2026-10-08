# 0633 — SMT — `.smt`

Variante testuale dello stesso formato, con suffisso canonico .smt.

Provenienza: copia del file originale `examples/#633 SMT/hello.smt2`.

Artefatto principale: `hello.smt`.

Controllo previsto, dalla cartella della variante:

```text
z3 -smt2 hello.smt
```

Risultato atteso: sat e ((greeting "Hello, World!"))..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://smt-lib.org/theories-UnicodeStrings.shtml](https://smt-lib.org/theories-UnicodeStrings.shtml)
