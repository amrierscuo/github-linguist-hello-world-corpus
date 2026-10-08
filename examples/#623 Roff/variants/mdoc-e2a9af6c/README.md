# 0623 — Roff — `.mdoc`

Manuale BSD mdoc con macro semantiche.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.mdoc`.

Controllo previsto, dalla cartella della variante:

```text
groff -Tascii -mdoc hello.mdoc
```

Risultato atteso: testo formattato contenente Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.gnu.org/software/groff/manual/groff.html](https://www.gnu.org/software/groff/manual/groff.html)
