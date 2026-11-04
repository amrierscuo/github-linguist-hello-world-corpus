# #194 Emacs Lisp

Voce e ordine canonici di `reference/languages.yml`.

Upload a batch Emacs Lisp script and print Hello, World! followed by newline.

## Toolchain and reproduction

GNU Emacs 29.3. Run from the example folder:

```sh
emacs -Q --batch --script hello.el
emacs -Q --batch --load variants/ext-emacs-2e656d616373/hello.emacs
emacs -Q --batch --eval '(require '"'"'desktop)' --load variants/ext-emacs-desktop-2e656d6163732e6465736b746f70/hello.emacs.desktop --eval '(progn (unless (equal corpus-greeting "Hello, World!") (error "Wrong restored greeting")) (princ corpus-greeting))'
```

Tre invocazioni native distinte caricano i tre suffissi. Le prime due stampano il saluto. La fixture desktop definisce corpus-greeting: il controllo carica desktop.el e il file completo, quindi verifica e stampa la variabile ripristinata. Il ripristino grafico di una sessione non fa parte di questa prova.

`-Q` disables the personal configuration of Emacs.

## State and Test

syntax and behavior verified `2026-10-08T23:33:35.178799+00:00`. Real result: `Hello, World!`.

[Log della verifica](verification/runtime.json) con comandi, versioni, output, exit code e SHA-256 dei file effettivamente controllati.

## Primary sources

- [https://github.com/emacs-mirror/emacs/blob/master/doc/lispref/streams.texi](https://github.com/emacs-mirror/emacs/blob/master/doc/lispref/streams.texi)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.el` | [hello.el](hello.el) syntax and behavior verified |
| `.emacs` | [hello.emacs](variants/ext-emacs-2e656d616373/hello.emacs) syntax and behavior verified |
| `.emacs.desktop` | [hello.emacs.desktop](variants/ext-emacs-desktop-2e656d6163732e6465736b746f70/hello.emacs.desktop) syntax and behavior verified |
