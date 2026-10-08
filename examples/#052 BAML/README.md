# #052 BAML

Voce canonica: `BAML`, tipo `programming`, `language_id: 502521509`.

Definire in BAML una funzione Hello con risposta strutturata il cui campo message è vincolato al letterale Hello, World!.

## Toolchain e riproduzione

Official BoundaryML BAML CLI — 0.226.2. Ambiente della prova: **Windows x64**.

Installare localmente @boundaryml/baml@0.226.2. generators.baml fissa la versione e l’output TypeScript; il verificatore ha generato 14 file in una copia isolata sotto work.

Comando/procedura dalla directory dell’esempio:

```text
npx baml-cli generate --from baml_src; BAML playground: eseguire GreetingForWorld con client configurato.
```

Risultato atteso: Generazione client TypeScript riuscita; chiamata modello attesa con message esattamente Hello, World! (non eseguita).

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Il compilatore BAML autentico ha accettato class, funzione, prompt, literal type e test. Il codice generato non viene incluso nel corpus. La chiamata al modello non è stata effettuata e non viene usato un mock come prova semantica.

Requisiti residui:

- Model invocation has not been performed; semantic greeting output and credentials remain pending.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://docs.boundaryml.com/ref/baml-cli/generate](https://docs.boundaryml.com/ref/baml-cli/generate)
- [https://github.com/BoundaryML/baml/blob/canary/fern/03-reference/baml/types.mdx](https://github.com/BoundaryML/baml/blob/canary/fern/03-reference/baml/types.mdx)
- [https://docs.boundaryml.com/ref/baml/test](https://docs.boundaryml.com/ref/baml/test)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.baml` | [generators.baml](baml_src/generators.baml), [hello.baml](baml_src/hello.baml) sintassi verificata |
