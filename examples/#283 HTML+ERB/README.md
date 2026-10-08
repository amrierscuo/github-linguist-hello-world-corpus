# #283 HTML+ERB

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Renderizzare HTML+ERB con un binding Ruby che fornisce audience=World.

ERB.new legge il template, result(binding) valuta l’interpolazione Ruby. Il driver originale confronta il documento prodotto dal motore ERB; non costruisce l’HTML mediante sostituzioni manuali.

## Toolchain e riproduzione

Ruby3.2.3, ERB della libreria standard

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
ruby render.rb
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://docs.ruby-lang.org/en/3.2/ERB.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.erb` | [hello.erb](hello.erb), [fixture.html.erb](variants/erb-deface-ad7ccb60/fixture.html.erb) creato, verifiche pendenti |
| `.erb.deface` | [hello.html.erb.deface](variants/erb-deface-ad7ccb60/hello.html.erb.deface) creato, verifiche pendenti |
| `.rhtml` | [hello.rhtml](variants/rhtml-6f031adf/hello.rhtml) creato, verifiche pendenti |
