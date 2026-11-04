# 0156 DNS Zone: variant `.arpa`

Role: Zone DNS reverse IPv4 for document block 192.0.2.0 / 24, with PTR and TXT greeting.

Type: **adapted**. Starting model: examples/#156 DNS Zone/hello.zone; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
named-checkzone 2.0.192.in-addr.arpa hello.arpa; named-compilezone -D -o <output>/canonical.zone 2.0.192.in-addr.arpa hello.arpa
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://bind9.readthedocs.io/en/latest/manpages.html#named-checkzone-zone-file-validation-tool](https://bind9.readthedocs.io/en/latest/manpages.html#named-checkzone-zone-file-validation-tool)
- [https://www.isc.org/bind/](https://www.isc.org/bind/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://bind9.readthedocs.io/en/latest/reference.html](https://bind9.readthedocs.io/en/latest/reference.html)
