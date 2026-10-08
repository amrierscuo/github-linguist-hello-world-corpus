# 0196 Erlang — variante `.xrl`

Ruolo: Specification Leex del lexer: restituisce il token greeting contenente il testo riconosciuto.

Tipo variante: **adapted**. Modello di partenza: examples/#196 Erlang/hello.erl; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
erl -noshell -eval 'leex:file("hello.xrl"), compile:file("hello.erl"), {ok,[{greeting,Text}],_}=hello:string("Hello, World!"), io:format("~s~n",[Text]), halt().'
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
- [https://www.erlang.org/doc/apps/parsetools/leex.html](https://www.erlang.org/doc/apps/parsetools/leex.html)
