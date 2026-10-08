# 0716 — Texinfo — `.txi`

Variante testuale dello stesso formato, con suffisso canonico .txi.

Provenienza: copia del file originale `examples/#716 Texinfo/hello.texi`.

Artefatto principale: `hello.txi`.

Controllo previsto, dalla cartella della variante:

```text
makeinfo --plaintext --output=work/hello.txt hello.txi
```

Risultato atteso: Documento renderizzato contiene Hello, World!..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html](https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html)
