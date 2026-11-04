# #380 Leo

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill Leo and return i13byte ASCII of Hello, World! as result of the transition main.

The Leo circuits return typic data instead of printing text: the transition exposes an array of13u8. program.json identifies the local program; no deploy or network transaction is required.

## Toolchain and reproduction

Leo/Aleo originale; versione da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
leo build
```

```text
leo run main
```

## Expected result and status

Output array [72u8,101u8,108u8,108u8,111u8,44u8,32u8,87u8,111u8,114u8,108u8,100u8,33u8].

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: Compiler/runtime Leo non preparati; build e valutazione locale pendenti.

## Primary sources

- https://github.com/ProvableHQ/leo
- https://provable.com/blog/introducing-the-leo-native-testing-framework

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.leo` | [main.leo](src/main.leo) created; verification pending |
