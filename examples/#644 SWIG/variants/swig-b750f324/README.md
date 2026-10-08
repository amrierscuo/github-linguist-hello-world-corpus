# 0644 — SWIG — `.swig`

Variante testuale dello stesso formato, con suffisso canonico .swig.

Provenienza: copia del file originale `examples/#644 SWIG/hello.i`.

Artefatto principale: `hello.swig`.

Controllo previsto, dalla cartella della variante:

```text
swig -python -outdir work -o work/hello_wrap.c hello.swig
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://swig.org/Doc4.3/SWIGDocumentation.html](https://swig.org/Doc4.3/SWIGDocumentation.html)
