# 0324: JSON: `.webapp`

Role: Manifest Open Web App Mozilla historical; greeting in the name.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
python -m json.tool hello.webapp; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Expected result: JSON document recognized in the specific scheme; greeting in the indicated field.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.webapp`: `568067ef9ab02bdeae81f0ebf54c60b50baf4d1930abf7491c2513bd3d44f58b`
- `index.html`: `67867b77f5bc7be02ee8c4788be7d073ef63a75ad317ee1d9b46193a52ee06f3`

Primary sources:

- https://firefox-source-docs.mozilla.org/devtools-user/app_manager/index.html
- https://www.rfc-editor.org/rfc/rfc8259

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
