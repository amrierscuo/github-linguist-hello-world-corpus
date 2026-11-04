# #156 DNS Zone

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Validate a DNS area and preserve a TXT greeting record with Hello, World! value.

The area contains SOA, NS, A for the nameserver and TXT of greeting. Use the reserved domain .example and the 192.0.2.1 documentation address. The original tool BIND controls syntax and integrity, without starting DNS server or changing resolver

## Toolchain and reproduction

ISC BIND named-checkzone 9.18.39-0ubuntu0.24.04.7-Ubuntu

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
named-checkzone -D -o normalized.zone corpus.example hello.zone
```

## Expected result and status

Zona accettata con serial 2026100801, OK ed exit 0; dump canonico conserva greeting.corpus.example. TXT "Hello, World!".

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://bind9.readthedocs.io/en/latest/manpages.html#named-checkzone-zone-file-validation-tool
- https://www.isc.org/bind/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zone` | [hello.zone](hello.zone) verified |
| `.arpa` | [hello.arpa](variants/ext-arpa-2e61727061/hello.arpa) created; verification pending |
