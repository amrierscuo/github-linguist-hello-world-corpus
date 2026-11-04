# 0045 AutoHotkey: variant `.ah1`

Role: Script AutoHotkey v1; syntax command, does not function v2.

Type: **adapted**. Starting model: examples/#045 AutoHotkey/hello.ahk; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
AutoHotkeyU64.exe /ErrorStdOut hello.ah1
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm](https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm)
- [https://www.autohotkey.com/download/2.0/](https://www.autohotkey.com/download/2.0/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.autohotkey.com/docs/v1/lib/FileAppend.htm](https://www.autohotkey.com/docs/v1/lib/FileAppend.htm)
