# 0325: JSON with Comments: `.sublime-build`

Role: Build system Sublime per program Original Node.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0 + jsonc-parser 3.3.1. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Aprire/interpretare con VS Code o Sublime Text secondo il ruolo; il file è solo un fixture e non viene installato nelle preferenze utente.
```

Expected result: Recognized configuration; inserimento/nome of greeting according to the role. For the theme: color rule, no emission of greeting.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `hello.sublime-build`: `4d438768c175b6a79d6e5a473bbdcfe6cb23a51aadeba46a0c08802d2bdced87`

Primary sources:

- https://www.sublimetext.com/docs/build_systems.html
- https://github.com/microsoft/node-jsonc-parser

Additive test actually performed:

Microsoft jsonc-parser performed actual JSONC parsing; the VS Code and Sublime application structures were not loaded.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.3.1
