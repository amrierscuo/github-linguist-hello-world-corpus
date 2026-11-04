# 0304: INI: `.cfg`

## Latest recorded verification

**Syntax and behavior verified** for `.cfg`. Unchanged suffix variant; main example status unchanged. [Recorded evidence](../../verification/native_20261104_followup_2e636667.json).

Ruolo: Configurazione INI generica.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 stdlib configparser. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Esaminare il file con il lettore originale del prodotto. Per unità systemd: systemd-analyze verify FILE (solo offline; non installare/avviare).
```

Expected result: the configuration is recognized and the specified value or description contains the greeting. This does not establish runtime behavior.

Status before this check: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.cfg`: `b053725e51f30830c476fe323a2ea0444893437282a774ade38021fb6a6cec34`

Primary sources:

- https://docs.python.org/3/library/configparser.html
