# 0180 Eagle — variante `.brd`

Ruolo: Documento PCB EAGLE XML con board/plain/text su layer tPlace; non schematic rinominato.

Tipo variante: **adapted**. Modello di partenza: examples/#180 Eagle/hello.sch; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Validatore EAGLE DTD originale: validare hello.brd; aprire in EAGLE/Fusion Electronics e leggere il testo sul board.
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

- [https://help.autodesk.com/cloudhelp/ENU/Fusion-ECAD/files/ECD-ULP-OBJECT-TYPES.htm](https://help.autodesk.com/cloudhelp/ENU/Fusion-ECAD/files/ECD-ULP-OBJECT-TYPES.htm)
- [https://github.com/github-linguist/linguist/blob/main/samples/Eagle/Eagle.sch](https://github.com/github-linguist/linguist/blob/main/samples/Eagle/Eagle.sch)
- [https://github.com/drtrigon/eagle/blob/master/doc/eagle.dtd](https://github.com/drtrigon/eagle/blob/master/doc/eagle.dtd)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://help.autodesk.com/view/EAGLE/ENU/](https://help.autodesk.com/view/EAGLE/ENU/)
