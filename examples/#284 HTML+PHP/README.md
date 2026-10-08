# #284 HTML+PHP

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire un template HTML+PHP ed ottenere il paragrafo Hello, World!.

Il template definisce audience in PHP e usa la forma <?= per interpolare htmlspecialchars. La verifica native lint precede l’esecuzione CLI; il markup esterno ai tag PHP viene preservato dal runtime.

## Toolchain e riproduzione

PHP CLI8.3.6, Zend Engine4.3.6, pacchetto Ubuntu8.3.6-0ubuntu0.24.04.11

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
php -n -l hello.phtml
```

```text
php -n hello.phtml
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.php.net/manual/en/language.basic-syntax.phpmode.php
- https://www.php.net/manual/en/function.htmlspecialchars.php

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.phtml` | [hello.phtml](hello.phtml) verificato |
