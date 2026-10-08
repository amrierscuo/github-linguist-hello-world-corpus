# 0176 ECL — variante `.eclxml`

Ruolo: Archivio ECLXML minimo redatto a mano secondo il consumer ufficiale EclCC::processXmlFile, che legge Query e Query/@originalFilename. Non si dichiara un export eseguito dal compilatore; la prova eclcc è ancora pendente.

Tipo variante: **adapted**. Modello di partenza: examples/#176 ECL/hello.ecl; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
eclcc -syntax hello.eclxml; per l’esecuzione compilare/inviare questo archivio a un ambiente HPCC locale di prova e confrontare OUTPUT.
```

Risultato atteso: eclcc legge l’archivio e accetta la query OUTPUT; l’esecuzione HPCC produce Hello, World!.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html](https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html)
- [https://hpccsystems.com/training/documentation/learning-ecl/](https://hpccsystems.com/training/documentation/learning-ecl/)
- [https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp](https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.cpp](https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.cpp)
