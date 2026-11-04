# #418 Markdown

Analyze Markdown CommonMark and make greetings as HTML title.

Canonical type `prose`, language_id `222`.

Suggested toolchain: Python 3.13 and markdown-it-py.

From the example directory:

```sh
python verify.py
```

Expected result: HTML <h1> Hello, World! </h1> and LF; stdout greeting and LF.

The README is documentation; hello.md is the separate primary Markdown artifact.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + markdown-it-py 4.2.0. [Log](verification/result.json).

Sources:

- [CommonMark — specifica](https://spec.commonmark.org/0.31.2/)
- [markdown-it-py — motore](https://github.com/executablebooks/markdown-it-py)

Install the dependencies in a separate directory:

```sh
python -m pip install markdown-it-py==4.2.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.md` | [hello.md](hello.md) verified |
| `.livemd` | [hello.livemd](variants/livemd-1b19eac1/hello.livemd) created; verification pending |
| `.markdown` | [hello.markdown](variants/markdown-7e4cc6af/hello.markdown) created; verification pending |
| `.mdown` | [hello.mdown](variants/mdown-c553b9ee/hello.mdown) created; verification pending |
| `.mdwn` | [hello.mdwn](variants/mdwn-d13c3a39/hello.mdwn) created; verification pending |
| `.mkd` | [hello.mkd](variants/mkd-ce2bdbce/hello.mkd) created; verification pending |
| `.mkdn` | [hello.mkdn](variants/mkdn-ba8fcdf1/hello.mkdn) created; verification pending |
| `.mkdown` | [hello.mkdown](variants/mkdown-f8609122/hello.mkdown) created; verification pending |
| `.ronn` | [hello.ronn](variants/ronn-8655d3d6/hello.ronn) created; verification pending |
| `.scd` | [hello.scd](variants/scd-4dd9ca08/hello.scd) created; verification pending |
| `.workbook` | [hello.workbook](variants/workbook-18c428ee/hello.workbook) created; verification pending |
