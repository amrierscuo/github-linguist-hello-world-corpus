# #542 Pod 6

Voce e ordine canonici di reference/languages.yml. Documento originale.

## Goal

Analyze and render a Pod6/Rakudoc document with Hello, World!.

Original Pod6 document really analyzed and rendered by Rakudo. The driver uses the relocated MoarVM runtime; the verification concerns documentation Pod6, not POD5 Perl.

## Toolchain and reproduction

Rakudo/MoarVM2022.12 original, parser Pod6 and maker Pod::To::Text. Versioni/provenienza and SHA-256 in the log; isolated dependencies in work.

```text
raku --doc=Text hello.pod6
```

## Expected result and status

Text rendered contains Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

verification/toolchain.json records SHA source - 256, actual command, exit/stdout/stderr and original runtime. The direct call to MoarVM in the log serves to relocate Rakudo without global installation.

## Primary sources

- https://docs.raku.org/language/pod
- https://rakudo.org/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pod` | [hello.pod](variants/pod-539ee4a9/hello.pod) created; verification pending |
| `.pod6` | [hello.pod6](hello.pod6) verified |
