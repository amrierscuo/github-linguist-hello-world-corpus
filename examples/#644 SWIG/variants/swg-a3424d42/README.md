# 0644 — SWIG — `.swg`

Variante testuale dello stesso formato, con suffisso canonico .swg.

Provenienza: copia del file originale `examples/#644 SWIG/hello.i`.

Artefatto principale: `hello.swg`.

Controllo previsto, dalla cartella della variante:

```text
swig -python -outdir work -o work/hello_wrap.c hello.swg
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://swig.org/Doc4.3/SWIGDocumentation.html](https://swig.org/Doc4.3/SWIGDocumentation.html)
