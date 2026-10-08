# 0623 — Roff — `.9`

Pagina man originale della sezione 9; .in è un template statico senza sostituzioni.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.9`.

Controllo previsto, dalla cartella della variante:

```text
groff -Tascii -man hello.9
```

Risultato atteso: testo formattato contenente Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.gnu.org/software/groff/manual/groff.html](https://www.gnu.org/software/groff/manual/groff.html)
