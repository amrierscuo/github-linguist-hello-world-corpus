# 0007 AGS Script — variante `.ash`

Ruolo: Header AGS con dichiarazione della funzione globale implementata nel companion.

Tipo variante: **adapted**. Modello di partenza: examples/#007 AGS Script/room1.asc; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
In un progetto AGS di prova: importare hello.ash come script header e greeting.asc come global script; chiamare ShowCorpusGreeting() da un evento.
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

- [https://adventuregamestudio.github.io/ags-manual/Globalfunctions_Message.html](https://adventuregamestudio.github.io/ags-manual/Globalfunctions_Message.html)
- [https://adventuregamestudio.github.io/ags-manual/EventTypes.html](https://adventuregamestudio.github.io/ags-manual/EventTypes.html)
- [https://adventuregamestudio.github.io/ags-manual/DistGame.html](https://adventuregamestudio.github.io/ags-manual/DistGame.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://adventuregamestudio.github.io/ags-manual/ImportingFunctionsAndVariables.html](https://adventuregamestudio.github.io/ags-manual/ImportingFunctionsAndVariables.html)
