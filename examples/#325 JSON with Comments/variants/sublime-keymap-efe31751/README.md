# 0325: JSON with Comments: `.sublime-keymap`

Role: Illustrative Binding keys to insert greeting.

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

- `hello.sublime-keymap`: `df2967265fe55edf7016e13998b23acb977f1218cfe652be5ff727d57b40339e`

Primary sources:

- https://www.sublimetext.com/docs/key_bindings.html
- https://github.com/microsoft/node-jsonc-parser

Additive test actually performed:

Microsoft jsonc-parser performed actual JSONC parsing; the VS Code and Sublime application structures were not loaded.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.3.1
