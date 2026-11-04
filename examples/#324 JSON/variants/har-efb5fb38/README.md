# 0324: JSON: `.har`

Role: Fixture HTTP Archive 1.2 with body greeting response; date and URL illustrative, no request made.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 json standard library. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Validatore HAR 1.2 e lettura log.entries[0].response.content.text
```

Expected result: Hello, World! in the represented body

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.har`: `dd45b3f0696a090659966c56890432a14f75d5bb6d600e647ddaf12668f98f78`

Primary sources:

- https://w3c.github.io/web-performance/specs/HAR/Overview.html
- https://www.rfc-editor.org/rfc/rfc8259

Additive test actually performed:

Parsing JSON/JSON Lines real of the canonical grammar alone; no progetto/configurazione application scheme has been validated.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.13.9
