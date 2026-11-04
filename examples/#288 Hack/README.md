# #288 Hack

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run the Hack entry point and print Hello, World!.

Il sorgente Hack dichiara <<__EntryPoint>> e main():void, con concatenazione ed echo. Il tag <?hh non è richiesto nei file .hack moderni. PHP non verifica questo punto di ingresso o il sistema di tipi Hack.

## Toolchain and reproduction

HHVM/Hack e typechecker hh_client; versioni effettive da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Con progetto Hack appropriato: hh_client
```

```text
hhvm hello.hack
```

## Expected result and status

stdout Hello, World! seguito da newline.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: HHVM/Hack and typechecker not available; verification pending.

## Primary sources

- https://docs.hhvm.com/hack/source-code-fundamentals/program-structure/
- https://hacklang.org/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hack` | [hello.hack](hello.hack), [driver.hack](variants/hhi-b673df30/driver.hack) created; verification pending |
| `.hh` | [hello.hh](variants/hh-bc9ff2ca/hello.hh) created; verification pending |
| `.hhi` | [hello.hhi](variants/hhi-b673df30/hello.hhi) created; verification pending |
| `.php` | [hello.php](variants/php-7410d4a4/hello.php) created; verification pending |
