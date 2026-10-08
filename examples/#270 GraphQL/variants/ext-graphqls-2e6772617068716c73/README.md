# 0270 GraphQL — variante `.graphqls`

Ruolo: Schema GraphQL SDL, distinto dal documento di operazione; copia byte-identica dello schema nativo originale.

Tipo variante: **alias**. Copia byte-identica di examples/#270 GraphQL/schema.graphql

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
GraphQL buildSchema(readFileSync("hello.graphqls")); query { greeting } con resolver saluto e confronto risultato.
```

Risultato atteso: greeting=Hello, World!; controllo Reader e input null corretti; PASS.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.graphql-js.org/docs/](https://www.graphql-js.org/docs/)
- [https://github.com/graphql/graphql-js](https://github.com/graphql/graphql-js)
- [https://spec.graphql.org/](https://spec.graphql.org/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
