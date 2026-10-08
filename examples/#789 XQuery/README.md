# #789 XQuery

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Valutare XQuery3.1 e restituire Hello, World!.

Saxon analizza e valuta la variabile/concat. Su Windows usare ; come separatore del classpath al posto di :.

## Toolchain e riproduzione

Saxon-HE12.9 originale e XML Resolver5.3.3, OpenJDK21

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
java -cp "saxon-he.jar:xmlresolver.jar" net.sf.saxon.Query -q:hello.xq "!method=text"
```

## Risultato atteso e stato

Hello, World! serializzato come testo.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.w3.org/TR/xquery-31/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xquery` | [hello.xquery](variants/xquery-d1e42ae2/hello.xquery) creato, verifiche pendenti |
| `.xq` | [hello.xq](hello.xq), [main.xq](variants/xqm-6120106c/main.xq) creato, verifiche pendenti |
| `.xql` | [hello.xql](variants/xql-598d9a0b/hello.xql) creato, verifiche pendenti |
| `.xqm` | [hello.xqm](variants/xqm-6120106c/hello.xqm) creato, verifiche pendenti |
| `.xqy` | [hello.xqy](variants/xqy-27e37189/hello.xqy) creato, verifiche pendenti |
