# #541 Pod

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare POD e renderizzare il saluto Hello, World! come documentazione.

hello.pod contiene direttive POD e un paragrafo originale. Il driver usa il parser/render originale della libreria Perl.

## Toolchain e riproduzione

Perl5.38.2, Pod::Simple::Text originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
perl render.pl
```

## Risultato atteso e stato

Testo renderizzato contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://perldoc.perl.org/perlpod
- https://perldoc.perl.org/Pod::Simple::Text

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pod` | [hello.pod](hello.pod) verificato |
