# #728 Twig

Renderizzare un template Twig con default ed escaping.

## Riproduzione

Toolchain: PHP 8.3.6; Twig 3.8.0. Ambiente della prova: Ubuntu 24.04 WSL2 x86_64.

```text
PHP con autoload Twig: creare FilesystemLoader("."), Environment(autoescape="html") e renderizzare hello.twig con name=World, senza name e con name=<World>. Il log include il comando PHP esatto.
```

Risultato atteso: Hello, World!

## Verifica

Sintassi e semantica verificate il 2026-10-08T23:32:27.905963+00:00. Le varianti hanno prove separate nel log quando consumate.

[Prova nativa](verification/finish_native.json) contiene versioni, comandi reali, exit code, output e SHA-256. I percorsi locali sono sostituiti da segnaposto. Compilati e dipendenze restano fuori dal corpus.

## Fonti primarie

- [https://twig.symfony.com/doc/3.x/](https://twig.symfony.com/doc/3.x/)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.twig` | [hello.twig](hello.twig) sintassi e semantica verificate |
