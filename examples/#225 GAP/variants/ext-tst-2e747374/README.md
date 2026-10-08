# 0225 GAP — variante `.tst`

Ruolo: Transcript di test GAP tst con prompt e risultato atteso, non script g rinominato.

Tipo variante: **adapted**. Modello di partenza: examples/#225 GAP/hello.g; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gap -q -c 'Test("hello.tst"); QUIT_GAP(0);'
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

- [https://docs.gap-system.org/doc/tut/manual.pdf](https://docs.gap-system.org/doc/tut/manual.pdf)
- [https://www.gap-system.org/](https://www.gap-system.org/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.gap-system.org/doc/ref/chap7.html](https://docs.gap-system.org/doc/ref/chap7.html)
