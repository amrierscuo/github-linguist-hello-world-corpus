# #194 Emacs Lisp

Voce e ordine canonici di `reference/languages.yml`.

Caricare uno script Emacs Lisp in batch e stampare Hello, World! seguito da newline.

## Toolchain e riproduzione

GNU Emacs 29.3. Eseguire dalla cartella dell'esempio:

```sh
emacs -Q --batch --script hello.el
emacs -Q --batch --load variants/ext-emacs-2e656d616373/hello.emacs
emacs -Q --batch --eval '(require '"'"'desktop)' --load variants/ext-emacs-desktop-2e656d6163732e6465736b746f70/hello.emacs.desktop --eval '(progn (unless (equal corpus-greeting "Hello, World!") (error "Wrong restored greeting")) (princ corpus-greeting))'
```

Tre invocazioni native distinte caricano i tre suffissi. Le prime due stampano il saluto. La fixture desktop definisce corpus-greeting: il controllo carica desktop.el e il file completo, quindi verifica e stampa la variabile ripristinata. Il ripristino grafico di una sessione non fa parte di questa prova.

`-Q` disabilita la configurazione personale di Emacs. La prova si esegue in batch.

## Stato e prova

Sintassi e semantica verificate il `2026-10-08T23:33:35.178799+00:00`. Risultato reale: `Hello, World!`.

[Log della verifica](verification/runtime.json) con comandi, versioni, output, exit code e SHA-256 dei file effettivamente controllati.

## Fonti primarie

- [https://github.com/emacs-mirror/emacs/blob/master/doc/lispref/streams.texi](https://github.com/emacs-mirror/emacs/blob/master/doc/lispref/streams.texi)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.el` | [hello.el](hello.el) sintassi e semantica verificate |
| `.emacs` | [hello.emacs](variants/ext-emacs-2e656d616373/hello.emacs) sintassi e semantica verificate |
| `.emacs.desktop` | [hello.emacs.desktop](variants/ext-emacs-desktop-2e656d6163732e6465736b746f70/hello.emacs.desktop) sintassi e semantica verificate |
