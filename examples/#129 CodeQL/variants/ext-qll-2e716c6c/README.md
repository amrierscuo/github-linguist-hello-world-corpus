# 0129 CodeQL — variante `.qll`

Ruolo: Libreria CodeQL .qll esporta una funzione, importata dalla query companion.

Tipo variante: **adapted**. Modello di partenza: examples/#129 CodeQL/hello.ql; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
codeql query compile consumer.ql; codeql query run consumer.ql --database=<database-C-piccolo-esterno>
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://codeql.github.com/docs/ql-language-reference/queries/](https://codeql.github.com/docs/ql-language-reference/queries/)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://codeql.github.com/docs/ql-language-reference/modules/](https://codeql.github.com/docs/ql-language-reference/modules/)
