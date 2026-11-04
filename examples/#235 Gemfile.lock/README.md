# #235 Gemfile.lock

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Generate and use a real Gemfile.lock to solve Rake and print Hello, World!.

Gemfile.lock è prodotto da una risoluzione autentica di Bundler, senza inventare checksum o versioni. Gemfile e Rakefile sono fixture originali. Il log registra l’installazione locale della gem ufficiale in work, lock/check ed esecuzione Bundler; Ruby viene invocato esplicitamente per evitare shebang di sistema.

## Toolchain and reproduction

Ruby 3.2.3; RubyGems pacchetto 3.4.20; Bundler dichiara 2.4.19 (pacchetto Ubuntu 2.4.20-1); Rake 13.3.0

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
gem install --local rake-13.3.0.gem --no-document
bundle lock --local
bundle check
```

```text
bundle exec rake
```

## Expected result and status

Dipendenze soddisfatte e task Rake predefinito produce stdout Hello, World! seguito da newline.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://bundler.io/man/bundle-lock.1.html
- https://bundler.io/man/bundle-exec.1.html
- https://rubygems.org/gems/rake/versions/13.3.0
