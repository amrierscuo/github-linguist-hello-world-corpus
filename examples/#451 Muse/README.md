# #451 Muse

Voce canonica `Muse`, tipo `prose`, language_id `474864066`.

Publish an original Emacs Muse document in HTML with greeting in the body.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Emacs Muse and muse-html/muse-publish. libraries The documented procedure publishes in the current directory.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Aprire hello.muse in Emacs con Muse attivo; M-x muse-project-publish-this-file; selezionare lo stile html.
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Motor Emacs Muse absent; title and paragraph are original Muse source.

Remaining requirements:

- Emacs Muse publishing engine is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.gnu.org/software/emacs-muse/manual/muse.html](https://www.gnu.org/software/emacs-muse/manual/muse.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.muse` | [hello.muse](hello.muse) created; verification pending |
