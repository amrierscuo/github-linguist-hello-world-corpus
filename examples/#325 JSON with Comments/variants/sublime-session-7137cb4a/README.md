# 0325: JSON with Comments: `.sublime_session`

Role: JSONC data of the canon language; not a serialization of stato/sessione Original Sublime.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0 + jsonc-parser 3.3.1. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Parser JSONC originale sul file hello.sublime_session
```

Expected result: Given greeting Hello, World!; application scheme Sublime not verified.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.
- The schema/versione of the editor status is unknown; this fixture should not be imported as the editor’s session or cache.

SHA-256 of variant files:

- `hello.sublime_session`: `a6b0590ded57cdec36711b0e2419126863803a761388ceccacb1dcadcb650ac0`

Primary sources:

- https://github.com/microsoft/node-jsonc-parser
- https://www.sublimetext.com/docs/projects.html

Additive test actually performed:

Microsoft jsonc-parser performed actual JSONC parsing; the VS Code and Sublime application structures were not loaded.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.3.1
