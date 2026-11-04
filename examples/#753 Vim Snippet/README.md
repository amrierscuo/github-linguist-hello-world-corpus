# #753 Vim Snippet

Expand a snippet UltiSnips to get greeting.

Canonical type `markup`, language_id `81265970`.

Suggested toolchain: Vim with original UltiSnips.

From the example directory:

```sh
Caricare hello.snippets come filetype fixture; digitare hello e attivare l’espansione.
```

Expected result: buffer contains Hello, World!.

Verification requires loader and expander, not a parser invented for these three lines.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [UltiSnips](https://github.com/SirVer/ultisnips/blob/master/doc/UltiSnips.txt)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.snip` | [hello.snip](variants/snip-4fb5d1ae/hello.snip) created; verification pending |
| `.snippet` | [hello.snippet](variants/snippet-29acba5e/hello.snippet) created; verification pending |
| `.snippets` | [hello.snippets](hello.snippets) created; verification pending |
