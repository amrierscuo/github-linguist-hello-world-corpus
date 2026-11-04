# 0324: JSON: `.jsonl`

Role: JSON Lines: independent JSON record per line.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Lettore JSON Lines: decodificare ogni riga come JSON e leggere greeting
```

Expected result: A record with greeting Hello, World!

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.jsonl`: `fe8fe45846aa1ade756aca6481d1e341c35a442bbaa631dcdeb1cc1b621fad80`

Primary sources:

- https://jsonlines.org/
- https://www.rfc-editor.org/rfc/rfc8259

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
