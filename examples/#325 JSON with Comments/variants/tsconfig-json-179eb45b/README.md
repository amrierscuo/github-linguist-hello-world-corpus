# 0325: JSON with Comments: `.tsconfig.json`

Ruolo: Config TypeScript con fixture sorgente separato; non JSON generico.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0 + jsonc-parser 3.3.1. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
tsc -p hello.tsconfig.json; node build/hello.js
```

Expected result: Recognized configuration; inserimento/nome of greeting according to the role. For the theme: color rule, no emission of greeting.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.ts`: `dcc62e4a18325773332e645365de256e46ae08fd1609ff72edd1d7367ed4b632`
- `hello.tsconfig.json`: `1172df4baeffa57b7796a73888b6c7d05dd7ea7699daa1628067f59ef4e06fcc`

Primary sources:

- https://www.typescriptlang.org/tsconfig/
- https://github.com/microsoft/node-jsonc-parser

Additive test actually performed:

Microsoft jsonc-parser performed actual JSONC parsing; the VS Code and Sublime application structures were not loaded.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.3.1
