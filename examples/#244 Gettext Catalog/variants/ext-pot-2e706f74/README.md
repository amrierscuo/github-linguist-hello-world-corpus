# 0244 Gettext Catalog: variant `.pot`

Role: Template gettext POT: msgid contains the source text and msgstr is empty, distinct from the translated PO catalog.

Version type: **adapted**. Starting model: examples/#244 Gettext Catalog/hello.po; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
msgfmt --check --check-format hello.pot -o <output>/template.mo; gettext reader: controllare il msgid Hello, World! e la traduzione ancora vuota.
```

Expected result: valid template catalog; msgid Hello, World! not translated.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)
- [https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html](https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html)
- [https://docs.python.org/3/library/gettext.html](https://docs.python.org/3/library/gettext.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
