# #754 Vim script

Eseguire Vim script e registrare il messaggio di saluto.

Tipo canonico `programming`, language_id `388`.

Toolchain prevista: Vim.

Dalla cartella dell’esempio:

```sh
vim -Nu NONE -n -es -S hello.vim; leggere il messaggio con redir in un harness headless.
```

Risultato atteso: messaggio effettivo Hello, World!.

In modalità silenziosa il messaggio viene catturato con redir, senza aprire una UI.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Vim9 native script interpreter in headless mode. [Log](verification/result.json). 

Fonti:

- [Vim expression commands](https://vimhelp.org/eval.txt.html#%3Aechomsg)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vim` | [hello.vim](hello.vim), [make.vim](variants/vba-e8141d49/make.vim), [greeting.vim](variants/vba-e8141d49/greeting.vim), [make.vim](variants/vmb-7d7e8091/make.vim), [greeting.vim](variants/vmb-7d7e8091/greeting.vim) creato, verifiche pendenti |
| `.vba` | [hello.vba](variants/vba-e8141d49/hello.vba) creato, verifiche pendenti |
| `.vimrc` | [hello.vimrc](variants/vimrc-7b703895/hello.vimrc) creato, verifiche pendenti |
| `.vmb` | [hello.vmb](variants/vmb-7d7e8091/hello.vmb) creato, verifiche pendenti |
