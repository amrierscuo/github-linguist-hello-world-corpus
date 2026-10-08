# 0596 — Racket — `.rktd`

Datum Racket serializzabile: hash che conserva il saluto.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.rktd`.

Controllo previsto, dalla cartella della variante:

```text
racket -e '(displayln (hash-ref (call-with-input-file "hello.rktd" read) (quote greeting)))'
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.racket-lang.org/reference/reader.html](https://docs.racket-lang.org/reference/reader.html)
