# #235 Gemfile.lock

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Generare e usare un Gemfile.lock reale per risolvere Rake e stampare Hello, World!.

Gemfile.lock è prodotto da una risoluzione autentica di Bundler, senza inventare checksum o versioni. Gemfile e Rakefile sono fixture originali. Il log registra l’installazione locale della gem ufficiale in work, lock/check ed esecuzione Bundler; Ruby viene invocato esplicitamente per evitare shebang di sistema.

## Toolchain e riproduzione

Ruby 3.2.3; RubyGems pacchetto 3.4.20; Bundler dichiara 2.4.19 (pacchetto Ubuntu 2.4.20-1); Rake 13.3.0

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
gem install --local rake-13.3.0.gem --no-document
bundle lock --local
bundle check
```

```text
bundle exec rake
```

## Risultato atteso e stato

Dipendenze soddisfatte e task Rake predefinito produce stdout Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://bundler.io/man/bundle-lock.1.html
- https://bundler.io/man/bundle-exec.1.html
- https://rubygems.org/gems/rake/versions/13.3.0
