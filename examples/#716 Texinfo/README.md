# #716 Texinfo

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Renderizzare un documento Texinfo con Hello, World!.

Texi2any/makeinfo originale analizza nodi e direttive e genera testo semplice.

## Toolchain e riproduzione

GNU Texinfo7.1 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
makeinfo --plaintext --output=- hello.texi
```

## Risultato atteso e stato

Documento renderizzato contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.texinfo` | [hello.texinfo](variants/texinfo-67e352f4/hello.texinfo) creato, verifiche pendenti |
| `.texi` | [hello.texi](hello.texi) verificato |
| `.txi` | [hello.txi](variants/txi-415ac389/hello.txi) creato, verifiche pendenti |
