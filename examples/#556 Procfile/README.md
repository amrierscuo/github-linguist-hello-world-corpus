# #556 Procfile

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Validate and execute a local Procfile that starts the greeting process.

Foreman originale legge la dichiarazione greeting: ruby greeting.rb, avvia il processo locale e registra il saluto e la sua terminazione con exit0. Un launcher reloca soltanto il Ruby autentico nel PATH isolato. Nessun deploy Heroku è effettuato.

## Toolchain and reproduction

Foreman0.90.0, Thor1.4.0, Ruby3.2.3

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
foreman check -f Procfile; foreman start -f Procfile
```

## Expected result and status

Procfile valido; processo greeting emette Hello, World! e termina0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://devcenter.heroku.com/articles/procfile
- https://github.com/ddollar/foreman
