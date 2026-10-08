# 0656 — Shell — `.sh.in`

Variante testuale dello stesso formato, con suffisso canonico .sh.in.

Provenienza: copia del file originale `examples/#656 Shell/hello.sh`.

Artefatto principale: `hello.sh.in`.

Controllo previsto, dalla cartella della variante:

```text
sh -n hello.sh.in
sh hello.sh.in
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html)
