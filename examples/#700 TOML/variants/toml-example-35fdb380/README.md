# 0700 — TOML — `.toml.example`

Variante testuale dello stesso formato, con suffisso canonico .toml.example.

Provenienza: copia del file originale `examples/#700 TOML/hello.toml`.

Artefatto principale: `hello.toml.example`.

Controllo previsto, dalla cartella della variante:

```text
Python tomllib: parse hello.toml.example, assert greeting == "Hello, World!"
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://toml.io/en/v1.0.0](https://toml.io/en/v1.0.0)
