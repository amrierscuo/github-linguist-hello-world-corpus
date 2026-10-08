# 0194 Emacs Lisp — variante `.emacs.desktop`

Ruolo: Desktop Emacs Lisp: ripristina una variabile globale; non script init duplicato.

Tipo variante: **adapted**. Modello di partenza: examples/#194 Emacs Lisp/hello.el; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
emacs -Q --batch -l hello.emacs.desktop --eval "(princ corpus-greeting)"
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/emacs-mirror/emacs/blob/master/doc/lispref/streams.texi](https://github.com/emacs-mirror/emacs/blob/master/doc/lispref/streams.texi)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.gnu.org/software/emacs/manual/html_node/emacs/Saving-Emacs-Sessions.html](https://www.gnu.org/software/emacs/manual/html_node/emacs/Saving-Emacs-Sessions.html)
