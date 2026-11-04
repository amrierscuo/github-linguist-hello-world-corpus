# #754 Vim script

Run Vim script and record the greeting message.

Canonical type `programming`, language_id `388`.

Suggested toolchain: Vim.

From the example directory:

```sh
vim -Nu NONE -n -es -S hello.vim; leggere il messaggio con redir in un harness headless.
```

Expected result: actual message Hello, World!.

In silent mode the message is captured with redir, without opening a UI.

Recorded status: syntax verified; behavior verified. Toolchain: Vim9 native script interpreter in headless mode. [Log](verification/result.json).

Sources:

- [Vim expression commands](https://vimhelp.org/eval.txt.html#%3Aechomsg)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vim` | [hello.vim](hello.vim), [make.vim](variants/vba-e8141d49/make.vim), [greeting.vim](variants/vba-e8141d49/greeting.vim), [make.vim](variants/vmb-7d7e8091/make.vim), [greeting.vim](variants/vmb-7d7e8091/greeting.vim) created; verification pending |
| `.vba` | [hello.vba](variants/vba-e8141d49/hello.vba) created; verification pending |
| `.vimrc` | [hello.vimrc](variants/vimrc-7b703895/hello.vimrc) created; verification pending |
| `.vmb` | [hello.vmb](variants/vmb-7d7e8091/hello.vmb) created; verification pending |
