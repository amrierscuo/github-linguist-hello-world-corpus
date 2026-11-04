# 0771: Wikitext: `.wiki`

## Latest recorded verification

**Syntax and behavior verified** for `.wiki`. mwparserfromhell: heading AST and extracted plain-text greeting, not full MediaWiki rendering. [Recorded evidence](../../verification/native_20261104_followup_2e77696b69.json).

Textual variation of the same format, with canon suffix .wiki.

Origin: copy of the original `examples/#771 Wikitext/hello.mediawiki` file.

Artefatto principale: `hello.wiki`.

Control provided, from the folder of the variant:

```text
MediaWiki parser: render hello.wiki
```

Expected result: Title Greeting, text Hello, World! and PASS..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.mediawiki.org/wiki/Help:Formatting](https://www.mediawiki.org/wiki/Help:Formatting)
- [https://mwparserfromhell.readthedocs.io/en/latest/](https://mwparserfromhell.readthedocs.io/en/latest/)
