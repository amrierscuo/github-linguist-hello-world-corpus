# #786 XML Property List

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare una Property List XML e leggere Hello, World!.

Documento plist1.0 con un dizionario e una stringa. Il decoder plistlib legge il valore senza scaricare il DTD esterno.

## Toolchain e riproduzione

plistlib originale della libreria standard Python; versione nel log

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Dizionario {greeting: Hello, World!}.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.plist` | [hello.plist](hello.plist) verificato |
| `.stTheme` | [hello.stTheme](variants/sttheme-0e334249/hello.stTheme) creato, verifiche pendenti |
| `.tmCommand` | [hello.tmCommand](variants/tmcommand-e3f4e751/hello.tmCommand) creato, verifiche pendenti |
| `.tmLanguage` | [hello.tmLanguage](variants/tmlanguage-01c07e1d/hello.tmLanguage) creato, verifiche pendenti |
| `.tmPreferences` | [hello.tmPreferences](variants/tmpreferences-dbf56f6e/hello.tmPreferences) creato, verifiche pendenti |
| `.tmSnippet` | [hello.tmSnippet](variants/tmsnippet-e9563c64/hello.tmSnippet) creato, verifiche pendenti |
| `.tmTheme` | [hello.tmTheme](variants/tmtheme-86bf8af9/hello.tmTheme) creato, verifiche pendenti |
