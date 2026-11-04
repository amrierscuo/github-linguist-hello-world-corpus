# #771 Wikitext

Voce canonica `Wikitext`, tipo `prose`, language_id `228`.

Original Wikitext page with a Greeting title and greeting text in the body.

## Toolchain and reproduction

mwparserfromhell / Python 3.13.9, 0.7.2. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e mwparserfromhell 0.7.2 in ambiente isolato.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Title Greeting, text Hello, World! and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The existing Wikitext parser builds the AST; the driver controls title and text obtained from strip_code. The goal is the source page and its text view, without affirming a HTML rendering of the MediaWiki server.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.mediawiki.org/wiki/Help:Formatting](https://www.mediawiki.org/wiki/Help:Formatting)
- [https://mwparserfromhell.readthedocs.io/en/latest/](https://mwparserfromhell.readthedocs.io/en/latest/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mediawiki` | [hello.mediawiki](hello.mediawiki) verified |
| `.wiki` | [hello.wiki](variants/wiki-161d167f/hello.wiki) created; verification pending |
| `.wikitext` | [hello.wikitext](variants/wikitext-b2a94597/hello.wikitext) created; verification pending |
