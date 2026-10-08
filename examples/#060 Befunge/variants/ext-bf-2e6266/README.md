# 0060 Befunge — variante `.bf`

Ruolo: Griglia Befunge-93; il .bf appartiene a Befunge in questa cartella, distinto dai .bf Brainfuck.

Tipo variante: **alias**. Copia byte-identica di examples/#060 Befunge/hello.befunge

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Interprete Befunge-93 originale: caricare hello.bf e confrontare stdout.
```

Risultato atteso: Exit 0; stdout esattamente Hello, World! seguito da LF.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/catseye/Befunge-93](https://github.com/catseye/Befunge-93)
- [https://github.com/catseye/Befunge-93/blob/master/doc/Befunge-93.markdown](https://github.com/catseye/Befunge-93/blob/master/doc/Befunge-93.markdown)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
