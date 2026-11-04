# #638 SRecode Template

Voce e ordine canonici di `reference/languages.yml`.

Upload a SRecode template and enter Hello, World!.

## Toolchain and reproduction

GNU Emacs 29.3 + bundled SRecode. Run from the example folder:

```sh
emacs -Q --batch --script verify.el
```

The Checker empowers Semantic, compile hello.srt with srecode-compile-file and inserts files:greeting with srecode-insert. Check the text produced by AUDIENCE dictionary resolution.

`-Q` disables the personal configuration of Emacs.

## State and Test

syntax and behavior verified `2026-10-08T23:33:35.675753+00:00`. Real result: `Hello, World!`.

[Log della verifica](verification/runtime.json) con comandi, versioni, output, exit code e SHA-256 dei file effettivamente controllati.

## Primary sources

- [https://raw.githubusercontent.com/emacs-mirror/emacs/master/etc/srecode/default.srt](https://raw.githubusercontent.com/emacs-mirror/emacs/master/etc/srecode/default.srt)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.srt` | [hello.srt](hello.srt) syntax and behavior verified |
