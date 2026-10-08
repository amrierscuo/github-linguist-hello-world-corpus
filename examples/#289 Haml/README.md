# #289 Haml

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Renderizzare un template Haml che concatena Hello, e World! in un paragrafo.

%p definisce il tag e = introduce l’espressione Ruby. Haml::Template è il renderer originale; il driver fissa Haml6.3.0 per riproducibilità ed usa le gem registrate nel log, installate in work. Le dipendenze esplicite sono caricate dal renderer reale.

## Toolchain e riproduzione

Haml6.3.0, Temple0.10.7, Tilt2.9.0, Thor1.5.0; Ruby3.2.3

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
ruby render.rb
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://haml.info/docs/yardoc/file.REFERENCE.html
- https://github.com/haml/haml
- https://rubygems.org/gems/haml/versions/6.3.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.haml` | [hello.haml](hello.haml) verificato |
| `.haml.deface` | [hello.html.haml.deface](variants/haml-deface-a5c3691d/hello.html.haml.deface) creato, verifiche pendenti |
