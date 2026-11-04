# #660 Sieve

Fix a Sieve message offline based on the greeting in the Subject.

## Toolchain

Sieve compiler/test engine

## Procedure

sievec hello.sieve; sieve-test hello.sieve hello.eml; verificare fileinto INBOX.CorpusGreeting.

## Expected result

For fixtures Subject= Hello, World! the result is fileinto INBOX.CorpusGreeting.

## Status

Syntax and behavioral verification pending.

Original message with example.invalid addresses; scheduled verification offline, without shipments.

Remaining requirements:
- Sieve compiler/offline test engine unavailable.

## Primary sources

- [https://www.rfc-editor.org/rfc/rfc5228](https://www.rfc-editor.org/rfc/rfc5228)
- [https://doc.dovecot.org/2.3/configuration_manual/sieve/](https://doc.dovecot.org/2.3/configuration_manual/sieve/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sieve` | [hello.sieve](hello.sieve) created; verification pending |
