# #129 CodeQL

Voce canonica: `CodeQL`, tipo `programming`, `language_id: 424259634`.

Restituire una sola riga CodeQL con colonna greeting uguale a Hello, World! mediante concatenazione di stringhe.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede la CLI CodeQL autentica. qlpack.yml definisce un query pack locale senza dipendenze; la query costante non importa uno schema di analisi o librerie specifiche di un linguaggio. Il comando di valutazione è da verificare con la CLI disponibile; se essa richiede un database, usarne uno di prova locale compatibile.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
codeql query compile hello.ql; codeql query run hello.ql --output hello.bqrs; codeql bqrs decode --format=csv hello.bqrs
```

Risultato atteso: Query compilata; tabella con una colonna greeting e una riga Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il saluto è un valore della select QL, non un commento. Non è stata trovata la CLI e non sono stati compilati o decodificati risultati. Nessun repository remoto, token o account è un requisito per la preparazione locale di questo esempio.

Requisiti residui:

- CodeQL native CLI is unavailable; query compile/evaluation remains pending and requires no external repository/account.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://codeql.github.com/docs/ql-language-reference/queries/](https://codeql.github.com/docs/ql-language-reference/queries/)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-compile)
- [https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run](https://docs.github.com/en/code-security/reference/code-scanning/codeql/codeql-cli-manual/query-run)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ql` | [hello.ql](hello.ql), [consumer.ql](variants/ext-qll-2e716c6c/consumer.ql) creato, verifiche pendenti |
| `.qll` | [hello.qll](variants/ext-qll-2e716c6c/hello.qll) creato, verifiche pendenti |
