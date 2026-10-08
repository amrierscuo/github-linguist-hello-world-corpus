# 0596 — Racket — `.rktl`

File Racket da caricare in un namespace base, senza direttiva #lang.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.rktl`.

Controllo previsto, dalla cartella della variante:

```text
racket -I racket/base -f hello.rktl
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.racket-lang.org/reference/load.html](https://docs.racket-lang.org/reference/load.html)
