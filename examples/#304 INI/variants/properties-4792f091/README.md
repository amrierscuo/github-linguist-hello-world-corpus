# 0304: INI: `.properties`

## Latest recorded verification

**Syntax and behavior verified** for `.properties`. Unchanged suffix variant; main example status unchanged. [Recorded evidence](../../verification/native_20261104_followup_2e70726f70657274696573.json).

Role: Java properties: pair chiave/valore without section header.

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

- `hello.properties`: `b39cef82a809353ae1a2ab63aedeb0048b348dd4257df8c9733a7d29042ce150`

Primary sources:

- https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html
- https://docs.python.org/3/library/configparser.html
