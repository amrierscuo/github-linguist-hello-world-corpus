# #280 HTML

Voce canonica `HTML`, tipo `markup`, language_id `146`.

Analyze a valid HTML5 document and check the visible text of a heading h1 under main.

## Toolchain and reproduction

Existing html5lib strict HTML5 tree builder, 1.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

html5lib 1.1 su Python 3.13.9. Il documento include doctype, lingua, charset e title. Il parser strict solleva errori su parsing non conforme.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python -m pip install html5lib==1.1; python verify.py hello.html
```

Expected result: Zero errors parser; heading Hello, World!; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The test delegates tokenization and construction of the DOM to the existing parser HTML5; it controls title, language and text of the heading. The semantic scope is the DOM with visible content, without declaring a visual rendering of the pixels.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/)
- [https://html5lib.readthedocs.io/en/latest/](https://html5lib.readthedocs.io/en/latest/)
- [https://github.com/html5lib/html5lib-python](https://github.com/html5lib/html5lib-python)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.html` | [hello.html](hello.html) verified |
| `.hta` | [hello.hta](variants/ext-hta-2e687461/hello.hta) created; verification pending |
| `.htm` | [hello.htm](variants/ext-htm-2e68746d/hello.htm) created; verification pending |
| `.html.hl` | [hello.html.hl](variants/ext-html-hl-2e68746d6c2e686c/hello.html.hl) created; verification pending |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) created; verification pending |
| `.xht` | [hello.xht](variants/ext-xht-2e786874/hello.xht) created; verification pending |
| `.xhtml` | [hello.xhtml](variants/ext-xhtml-2e7868746d6c/hello.xhtml) created; verification pending |
