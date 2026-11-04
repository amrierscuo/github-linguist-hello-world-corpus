# #799 YASnippet

Voce e ordine canonici di `reference/languages.yml`.

Expand a YASnippet with the default World.

## Toolchain and reproduction

GNU Emacs 29.3 + original YASnippet 0.14.0. Run from the example folder:

```sh
emacs -Q --batch --load <YASnippet-0.14.0>/yasnippet.el --load verify.el
```

Install YASnippet original 0.14.0 and replace the path between angular brackets.The checker uses the original parser for metadata, records the snippet in text-mode, expands the trigger greeting and verification full text and placeholder 1 World still active.

`-Q` disables the personal configuration of Emacs.

## State and Test

syntax and behavior verified `2026-10-08T23:33:35.865605+00:00`. Real result: `Hello, World!`.

[Log della verifica](verification/runtime.json) con comandi, versioni, output, exit code e SHA-256 dei file effettivamente controllati.

## Primary sources

- [https://joaotavora.github.io/yasnippet/snippet-development.html](https://joaotavora.github.io/yasnippet/snippet-development.html)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.yasnippet` | [hello.yasnippet](hello.yasnippet) syntax and behavior verified |
