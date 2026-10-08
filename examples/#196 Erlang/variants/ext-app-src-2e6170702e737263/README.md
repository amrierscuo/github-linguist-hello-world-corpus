# 0196 Erlang — variante `.app.src`

Ruolo: Application resource Erlang di build (.app.src), da generare/installare come corpus_greeting.app.

Tipo variante: **adapted**. Modello di partenza: examples/#196 Erlang/hello.erl; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
erlc -o <output>/ebin greeting_app.erl; copiare hello.app.src come <output>/ebin/corpus_greeting.app; erl -pa <output>/ebin -noshell -eval "application:start(corpus_greeting), halt()."
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

- [https://www.erlang.org/doc/system/seq_prog.html](https://www.erlang.org/doc/system/seq_prog.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.erlang.org/doc/apps/kernel/app.html](https://www.erlang.org/doc/apps/kernel/app.html)
