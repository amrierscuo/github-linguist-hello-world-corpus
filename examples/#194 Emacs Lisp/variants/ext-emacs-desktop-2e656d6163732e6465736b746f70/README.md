# #194 Emacs Lisp variante `.emacs.desktop`

File originale con ruolo specifico del suffisso. Eseguito esplicitamente con GNU Emacs 29.3, senza ereditare la verifica di un altro file.

Dalla cartella principale dell'esempio:

```sh
emacs -Q --batch --eval '(require '"'"'desktop)' --load variants/ext-emacs-desktop-2e656d6163732e6465736b746f70/hello.emacs.desktop --eval '(progn (unless (equal corpus-greeting "Hello, World!") (error "Wrong restored greeting")) (princ corpus-greeting))'
```

Risultato reale `Hello, World!`, exit 0. Sintassi e semantica verificate il `2026-10-08T23:33:35.178799+00:00`.

[Log della verifica](../../verification/runtime.json) con comando e SHA-256 di questo file.

La fixture desktop ripristina corpus-greeting tramite caricamento Lisp. Il ripristino grafico di una sessione non fa parte della prova.
