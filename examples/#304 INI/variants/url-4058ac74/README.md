# 0304: INI: `.url`

Ruolo: Internet shortcut Windows con destinazione riservata example.invalid; nessuna navigazione.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 stdlib configparser. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Esaminare il file con il lettore originale del prodotto. Per unità systemd: systemd-analyze verify FILE (solo offline; non installare/avviare).
```

Expected result: the configuration is recognized and the specified value or description contains the greeting. This does not establish runtime behavior.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.url`: `e1c8b9df434dd7addb29756e8999aaf9e6b07619a4effe9fa390038b01ad2a91`

Primary sources:

- https://learn.microsoft.com/en-us/windows/win32/lwef/internet-shortcuts
- https://docs.python.org/3/library/configparser.html
