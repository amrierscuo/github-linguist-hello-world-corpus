# 0304: INI: `.mount`

Role: Explanatory mount systemd unit, to be validated offline without mounting.

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

- `tmp-corpus-hello.mount`: `0b9f6bb397f9a4215362e066a81dafc4012c56969143e73ad6d659cf286f1b0e`

Primary sources:

- https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
- https://docs.python.org/3/library/configparser.html
