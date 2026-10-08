# 0482 — OASv2-yaml: `.yml`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#482 OASv2-yaml/hello.yaml.

Toolchain richiesta: Node.js v22.20.0; {'@apidevtools/swagger-parser': '13.1.0', 'ajv': '8.20.0'}. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.yml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.yml`: `69f7c1b92a9e78cb976d08dde918a7c3ba0ed18a332456891fd80e7e60c83d9b`
- `package.json`: `02af28fa803a896a950d899f50bbc58f5a37142b119ef825a8882ec7b717774a`
- `verify.cjs`: `0abc61b66cac54cb7966da230a2f0de76d1bbd56a25c9800abba2b223f63db97`

Fonti primarie:

- https://spec.openapis.org/oas/v2.0.html
- https://apidevtools.com/swagger-parser/
- https://ajv.js.org/
