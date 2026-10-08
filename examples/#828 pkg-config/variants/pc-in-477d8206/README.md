# 0828 — pkg-config — `.pc.in`

Template pkg-config con placeholder Autoconf reali; richiede sostituzione prima dell’uso.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.pc.in`.

Controllo previsto, dalla cartella della variante:

```text
configure/CMake configure_file: replace @prefix@ with /corpus/example and @PACKAGE_VERSION@ with 1.0.0; write /absolute/work/pkg-config/hello.pc
PKG_CONFIG_PATH=/absolute/work/pkg-config pkg-config --variable=greeting hello
```

Risultato atteso: variabile greeting == Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://people.freedesktop.org/~dbn/pkg-config-guide.html](https://people.freedesktop.org/~dbn/pkg-config-guide.html)
