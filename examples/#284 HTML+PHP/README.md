# #284 HTML+PHP

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run a HTML template + PHP and get the Hello, World! paragraph.

Il template definisce audience in PHP e usa la forma <?= per interpolare htmlspecialchars. La verifica native lint precede l’esecuzione CLI; il markup esterno ai tag PHP viene preservato dal runtime.

## Toolchain and reproduction

PHP CLI8.3.6, Zend Engine4.3.6, pacchetto Ubuntu8.3.6-0ubuntu0.24.04.11

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
php -n -l hello.phtml
```

```text
php -n hello.phtml
```

## Expected result and status

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.php.net/manual/en/language.basic-syntax.phpmode.php
- https://www.php.net/manual/en/function.htmlspecialchars.php

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.phtml` | [hello.phtml](hello.phtml) verified |
