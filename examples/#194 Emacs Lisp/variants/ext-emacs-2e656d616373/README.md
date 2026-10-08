# #194 Emacs Lisp variante `.emacs`

File originale con ruolo specifico del suffisso. Eseguito esplicitamente con GNU Emacs 29.3, senza ereditare la verifica di un altro file.

Dalla cartella principale dell'esempio:

```sh
emacs -Q --batch --load variants/ext-emacs-2e656d616373/hello.emacs
```

Risultato reale `Hello, World!`, exit 0. Sintassi e semantica verificate il `2026-10-08T23:33:35.178799+00:00`.

[Log della verifica](../../verification/runtime.json) con comando e SHA-256 di questo file.

Il file di startup viene caricato realmente da Emacs in batch.
