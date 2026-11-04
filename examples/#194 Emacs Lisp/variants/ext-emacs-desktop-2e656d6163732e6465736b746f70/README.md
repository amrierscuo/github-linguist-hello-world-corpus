# #194 Emacs Lisp variante `.emacs.desktop`

Original file with specific role of the suffix.Explainly executed with GNU Emacs 29.3, without inherit the verification of another file.

From the main folder of the example:

```sh
emacs -Q --batch --eval '(require '"'"'desktop)' --load variants/ext-emacs-desktop-2e656d6163732e6465736b746f70/hello.emacs.desktop --eval '(progn (unless (equal corpus-greeting "Hello, World!") (error "Wrong restored greeting")) (princ corpus-greeting))'
```

Result real `Hello, World!`, exit 0. syntax and behavior verified `2026-10-08T23:33:35.178799+00:00`.

[Log della verifica](../../verification/runtime.json) with command and SHA-256 of this file.

The desktop fixture restores corpus-greeting via Lisp loading. The graphical restoration of a session is not part of the test.
