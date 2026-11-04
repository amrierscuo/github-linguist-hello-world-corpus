# 0324: JSON: `.webmanifest`

Role: Web App Manifest W3C; name of greeting and local page.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
python -m json.tool hello.webmanifest; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Expected result: JSON document recognized in the specific scheme; greeting in the indicated field.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.webmanifest`: `7f766e2bbc5f8f7d3fd390ed7aae9f975a14cc2e35ee6f0073e3cdc0d2194c7a`
- `index.html`: `67867b77f5bc7be02ee8c4788be7d073ef63a75ad317ee1d9b46193a52ee06f3`

Primary sources:

- https://www.w3.org/TR/appmanifest/
- https://www.rfc-editor.org/rfc/rfc8259

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
