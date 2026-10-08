# #689 SurrealQL

Voce canonica `SurrealQL`, tipo `programming`, language_id `735141027`.

Valutare un RETURN SurrealQL con concatenazione di stringhe.

## Toolchain e riproduzione

Required genuine surreal compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede SurrealDB CLI/engine originale con endpoint memory compatibile.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
surreal sql --endpoint memory --namespace corpus --database greeting < hello.surql
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Query originale, locale e senza record persistenti; engine non configurato.

Requisiti residui:

- Required surreal toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://surrealdb.com/docs/surrealql/statements/return](https://surrealdb.com/docs/surrealql/statements/return)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.surql` | [hello.surql](hello.surql) creato, verifiche pendenti |
