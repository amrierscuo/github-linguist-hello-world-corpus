# 0324: JSON: `.4DForm`

Role: Form 4D with static text object, in the hierarchy Sources/Forms/Greeting/form.4DForm.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
python -m json.tool hello.4DForm; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Expected result: JSON document recognized in the specific scheme; greeting in the indicated field.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.4DForm`: `0030ae7e45ad7e663d323055ba64dbf1819bd8fb5b3b4d8c15f0f4036f4fbf89`

Primary sources:

- https://developer.4d.com/docs/18/FormObjects/text
- https://developer.4d.com/docs/18/Project/architecture
- https://www.rfc-editor.org/rfc/rfc8259

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
