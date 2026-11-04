# 0325: JSON with Comments: `.sublime-settings`

Role: Settings Sublime; corpus_greeting is a custom data key for future plugins, not an option that prints text.

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

- `hello.sublime-settings`: `b1b50ee2e7bf3fda8cb4ea127d351b7febb32abfdd06a5c47e54f7469debdce7`

Primary sources:

- https://www.sublimetext.com/docs/settings.html
- https://github.com/microsoft/node-jsonc-parser

Additive test actually performed:

Microsoft jsonc-parser performed actual JSONC parsing; the VS Code and Sublime application structures were not loaded.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 3.3.1
