# 0280 HTML — variante `.html.hl`

Ruolo: Pagina nel sottoinsieme HTML comune; .html.hl resta formato HTML/Hoplon, non sorgente ClojureScript .cljs.hl.

Tipo variante: **alias**. Copia byte-identica di examples/#280 HTML/hello.html

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Reader HTML del modello: caricare hello.html.hl e controllare il DOM h1; per .html.hl usare inoltre il frontend HTML/Hoplon dedicato.
```

Risultato atteso: Zero errori parser; heading Hello, World!; PASS.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/)
- [https://html5lib.readthedocs.io/en/latest/](https://html5lib.readthedocs.io/en/latest/)
- [https://github.com/html5lib/html5lib-python](https://github.com/html5lib/html5lib-python)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
