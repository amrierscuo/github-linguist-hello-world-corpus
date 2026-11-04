# #728 Twig

Render a Twig template with default and escaping.

## Reproduction

Toolchain: PHP 8.3.6; Twig 3.8.0. Test environment: Ubuntu 24.04 WSL2 x86_64.

```text
PHP con autoload Twig: creare FilesystemLoader("."), Environment(autoescape="html") e renderizzare hello.twig con name=World, senza name e con name=<World>. Il log include il comando PHP esatto.
```

Expected result: Hello, World!

## Verification

syntax and behavior verified 2026-10-08T23:32:27.905963+00:00. The variants have separate evidence in the log when consumed.

[Prova nativa](verification/finish_native.json) contains versions, real commands, exit code, output and SHA-256. The local routes are replaced by placeholders.

## Primary sources

- [https://twig.symfony.com/doc/3.x/](https://twig.symfony.com/doc/3.x/)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.twig` | [hello.twig](hello.twig) syntax and behavior verified |
