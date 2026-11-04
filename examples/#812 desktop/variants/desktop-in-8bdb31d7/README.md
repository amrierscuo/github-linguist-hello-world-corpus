# 0812: desktop: `.desktop.in`

Textual variation of the same format, with canon suffix .desktop.in.

Origin: copy of the original `examples/#812 desktop/hello.desktop` file.

Artefatto principale: `hello.desktop.in`.

Control provided, from the folder of the variant:

```text
desktop-file-validate hello.desktop.in
```

Expected result: Validator without errors; Name= Hello, World! and Exec recognized..

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://specifications.freedesktop.org/desktop-entry/latest/](https://specifications.freedesktop.org/desktop-entry/latest/)
