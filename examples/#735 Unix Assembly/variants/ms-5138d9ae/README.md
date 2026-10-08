# 0735 — Unix Assembly — `.ms`

Variante testuale dello stesso formato, con suffisso canonico .ms.

Provenienza: copia del file originale `examples/#735 Unix Assembly/hello.s`.

Artefatto principale: `hello.ms`.

Controllo previsto, dalla cartella della variante:

```text
as --64 hello.ms -o work/hello.o
ld work/hello.o -o work/hello
work/hello
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://sourceware.org/binutils/docs/as/](https://sourceware.org/binutils/docs/as/)
- [https://man7.org/linux/man-pages/man2/write.2.html](https://man7.org/linux/man-pages/man2/write.2.html)
