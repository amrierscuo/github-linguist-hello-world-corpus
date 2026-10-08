# #270 GraphQL

Voce canonica `GraphQL`, tipo `data`, language_id `139`.

Analizzare schema/query GraphQL, controllare i tipi ed eseguire una query parametrica con un resolver locale.

## Toolchain e riproduzione

Official GraphQL.js reference implementation — 16.11.0; Node.js 22.20.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

GraphQL.js ufficiale 16.11.0 e Node.js 22.20.0. Nessun server/account è necessario; i file schema.graphql e hello.graphql sono originali.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools graphql@16.11.0; node verify.cjs .tools
```

Risultato atteso: greeting=Hello, World!; controllo Reader e input null corretti; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova valida AST contro schema, esegue World e Reader e verifica l’errore per name=null. Il resolver locale calcola la stringa attraverso l’execution engine GraphQL autentico.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.graphql-js.org/docs/](https://www.graphql-js.org/docs/)
- [https://github.com/graphql/graphql-js](https://github.com/graphql/graphql-js)
- [https://spec.graphql.org/](https://spec.graphql.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.graphql` | [hello.graphql](hello.graphql), [schema.graphql](schema.graphql) verificato |
| `.gql` | [hello.gql](variants/ext-gql-2e67716c/hello.gql) creato, verifiche pendenti |
| `.graphqls` | [hello.graphqls](variants/ext-graphqls-2e6772617068716c73/hello.graphqls) creato, verifiche pendenti |
