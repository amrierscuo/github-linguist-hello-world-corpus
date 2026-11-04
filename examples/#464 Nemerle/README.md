# #464 Nemerle

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in Nemerle and print Hello, World!.

Hello module exposes Main():void; def defines audience and Console.WriteLine performs IO.

## Toolchain and reproduction

Compiler Nemerle/.NET originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
ncc -out:Hello.exe Hello.n
```

```text
Eseguire Hello.exe dopo compilazione.
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Compiler Nemerle not prepared.

## Primary sources

- https://github.com/rsdn/nemerle
- https://rsdn.org/article/Nemerle/TheNemerleLanguage.xml

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.n` | [Hello.n](Hello.n) created; verification pending |
