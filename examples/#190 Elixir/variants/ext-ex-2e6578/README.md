# 0190 Elixir — variante `.ex`

Ruolo: Sorgente compilabile Elixir .ex; il corpo top-level usa lo stesso linguaggio di .exs.

Tipo variante: **alias**. Copia byte-identica di examples/#190 Elixir/hello.exs

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
elixirc -o <output> hello.ex; verificare stdout della valutazione del corpo della unità Elixir.
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://elixir.hexdocs.pm/introduction.html](https://elixir.hexdocs.pm/introduction.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
