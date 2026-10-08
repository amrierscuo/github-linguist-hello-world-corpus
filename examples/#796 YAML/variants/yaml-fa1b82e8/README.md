# 0796 — YAML — `.yaml`

Documento YAML dello stesso formato; suffisso composito .yaml conservato esattamente. Il template è statico e non dichiara sostituzioni o una configurazione MySQL specifica.

Provenienza: copia del file originale `examples/#796 YAML/hello.yml`.

Artefatto principale: `hello.yaml`.

Controllo previsto, dalla cartella della variante:

```text
Python yaml.safe_load: parse hello.yaml; assert greeting == "Hello, World!"
```

Risultato atteso: Mapping con greeting = Hello, World!..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://pyyaml.org/wiki/PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
