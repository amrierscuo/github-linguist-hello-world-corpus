# #133 Common Lisp

## Latest recorded verification

Latest extension checks:
- `.asd`: SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Evidence](verification/native_20261105_batch_2e617364.json).
- `.cl`: SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Evidence](verification/native_20261105_batch_2e636c.json).
- `.l`: SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Evidence](verification/native_20261105_batch_2e6c.json).
- `.lisp`: SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Evidence](verification/native_20261105_batch_2e6c697370.json).
- `.lsp`: SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Evidence](verification/native_20261105_batch_2e6c7370.json).
- `.sexp`: SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Evidence](verification/native_20261105_batch_2e73657870.json).

Voce canonica: `Common Lisp`, tipo `programming`, `language_id: 66`.

Concatenare stringhe Common Lisp e scriverle sullo standard output con format.

## Toolchain and reproduction

Native SBCL Ubuntu distribution extracted locally, SBCL 2.2.9.debian. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

SBCL 2.2.9.debian from the Ubuntu package, extracted under work without global installation. For a local extraction set SBCL_HOME to the usr/lib/sbcl directory of the package.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
sbcl --script hello.lisp
```

Exit 0; stdout Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic SBCL reader and compiler perform the original form. concatenate uses the string result type; the ~A format directive writes the content and ~% adds newline.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://www.sbcl.org/manual/#Shebang-Scripts](https://www.sbcl.org/manual/#Shebang-Scripts)
- [https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm](https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm)
- [https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm](https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lisp` | [hello.lisp](hello.lisp), [greeting.lisp](variants/ext-asd-2e617364/greeting.lisp) syntax and behavior verified |
| `.asd` | [hello.asd](variants/ext-asd-2e617364/hello.asd) syntax and behavior verified |
| `.cl` | [hello.cl](variants/ext-cl-2e636c/hello.cl) syntax and behavior verified |
| `.l` | [hello.l](variants/ext-l-2e6c/hello.l) syntax and behavior verified |
| `.lsp` | [hello.lsp](variants/ext-lsp-2e6c7370/hello.lsp) syntax and behavior verified |
| `.ny` | [hello.ny](variants/ext-ny-2e6e79/hello.ny) created; verification pending |
| `.podsl` | [hello.podsl](variants/ext-podsl-2e706f64736c/hello.podsl) created; verification pending |
| `.sexp` | [hello.sexp](variants/ext-sexp-2e73657870/hello.sexp) syntax and behavior verified |