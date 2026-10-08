# 0682 — Starlark — `.bzl`

Modulo Starlark caricabile che restituisce il saluto.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.bzl`.

Controllo previsto, dalla cartella della variante:

```text
Bazel/Starlark load("//:hello.bzl", "greeting"); print(greeting())
```

Risultato atteso: valore Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://bazel.build/rules/language](https://bazel.build/rules/language)
