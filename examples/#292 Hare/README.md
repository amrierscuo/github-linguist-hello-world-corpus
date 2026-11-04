# #292 Hare

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill Hare and issue Hello, World! using fmt:printfln.

main is exported, audience is a constant string and Hello format, {}! replaces World. The operator! asserts the success of IO. The necessary toolchain includes the native components of Hare.

## Toolchain and reproduction

Hare, harec, backend QBE e assembler/linker; versioni effettive da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
hare build -o hello hello.ha
```

```text
./hello
```

## Expected result and status

stdout Hello, World! seguito da newline.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: Hare/harec e QBE non preparati; compiler e runtime pendenti.

## Primary sources

- https://harelang.org/tutorials/introduction/
- https://docs.harelang.org/fmt/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ha` | [hello.ha](hello.ha) created; verification pending |
