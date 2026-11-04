# 0324: JSON: `.geojson`

Role: Feature GeoJSON with Point and descriptive properties.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
python -m json.tool hello.geojson; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Expected result: JSON document recognized in the specific scheme; greeting in the indicated field.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.geojson`: `7d6a3e34642a7d6b6caac32155d1e574091b3372d94be1a653bfd6a84024d3c9`

Primary sources:

- https://www.rfc-editor.org/rfc/rfc7946
- https://www.rfc-editor.org/rfc/rfc8259

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
