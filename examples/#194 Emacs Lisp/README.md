# #194 Emacs Lisp

Caricare uno script Emacs Lisp in batch e stampare Hello, World! seguito da newline.

Tipo canonico `programming`, language_id `102`.

Toolchain prevista: GNU Emacs con interprete Emacs Lisp.

Dalla cartella dell’esempio:

```sh
emacs --batch -Q --script hello.el
```

Risultato atteso: stdout `Hello, World!\n`, uscita 0.

-Q disabilita i file di inizializzazione personali. princ stampa il contenuto della stringa senza virgolette, diversamente da prin1.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [GNU Emacs Lisp — funzioni di output, manuale originale](https://github.com/emacs-mirror/emacs/blob/master/doc/lispref/streams.texi)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.el` | [hello.el](hello.el) creato, verifiche pendenti |
| `.emacs` | [hello.emacs](variants/ext-emacs-2e656d616373/hello.emacs) creato, verifiche pendenti |
| `.emacs.desktop` | [hello.emacs.desktop](variants/ext-emacs-desktop-2e656d6163732e6465736b746f70/hello.emacs.desktop) creato, verifiche pendenti |
