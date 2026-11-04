# 0325: JSON with Comments: `.hujson`

Role: HuJSON: superset JSON with comments; this fixture uses the shared JSONC subset.

Origin: Copia byte-identica of the original corpus source: examples/#325 JSON with Comments/hello.jsonc.

Required toolchain: Node.js 22.20.0 + jsonc-parser 3.3.1. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.hujson; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Hello, World! and LF; no parsing error.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.hujson`: `4284fd1dd5b3626ea52df2ac06daccaef3605d1e510a41cd2969ef03e493aaed`
- `verify.cjs`: `8e0f9decdfa86c6106e75f58312b147912c4e75f81afe3587a63873b5339d35a`

Primary sources:

- https://github.com/tailscale/hujson
- https://github.com/microsoft/node-jsonc-parser

Additive test actually performed:

Microsoft jsonc-parser performed actual JSONC parsing; the VS Code and Sublime application structures were not loaded.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.3.1
