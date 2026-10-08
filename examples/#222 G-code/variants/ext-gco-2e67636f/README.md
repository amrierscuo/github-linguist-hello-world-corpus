# 0222 G-code — variante `.gco`

Ruolo: File dello stesso dialetto G-code: il controllo resta offline, con i dati/obiettivo del modello.

Tipo variante: **alias**. Copia byte-identica di examples/#222 G-code/hello.gcode

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Parser offline della stessa variante G-code del modello: leggere hello.gco e controllare la sequenza di comandi senza inviarli a una macchina.
```

Risultato atteso: Il comando M117 ha il messaggio Hello, World!; non contiene istruzioni di movimento.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://marlinfw.org/docs/gcode/M117.html](https://marlinfw.org/docs/gcode/M117.html)
- [https://github.com/AndyEveritt/GcodeParser](https://github.com/AndyEveritt/GcodeParser)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
