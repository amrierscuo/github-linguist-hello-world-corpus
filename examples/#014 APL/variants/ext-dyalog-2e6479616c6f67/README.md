# 0014 APL — variante `.dyalog`

Ruolo: Sorgente testuale APL/Dyalog, non un workspace binario DWS.

Tipo variante: **alias**. Copia byte-identica di examples/#014 APL/hello.apl

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Dyalog: caricare hello.dyalog come sorgente testuale e valutare il corpo nel workspace di prova.
```

Risultato atteso: Exit 0; stderr vuoto; stdout esattamente Hello, World! e un terminatore LF/CRLF (CRLF osservato su Windows) nel dialetto dzaima/APL.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/dzaima/APL](https://github.com/dzaima/APL)
- [https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/build](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/build)
- [https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/src/APL/Main.java](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/src/APL/Main.java)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
