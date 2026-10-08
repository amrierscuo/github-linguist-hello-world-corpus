# 0205 Fancy — variante `.fancypack`

Ruolo: Descriptor Fancy Package Specification con include_files e metadati, adattato dall’implementazione originale del package manager; nessuna dipendenza da installare.

Tipo variante: **adapted**. Modello di partenza: examples/#205 Fancy/hello.fy; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Fancy originale: File eval: "hello.fancypack"; confrontare description e include_files della Specification; eseguire greeting.fy separatamente.
```

Risultato atteso: Descriptor restituisce una Specification con description Hello, World! e include_files greeting.fy; companion stampa il saluto.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/bakkdoor/fancy](https://github.com/bakkdoor/fancy)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/bakkdoor/fancy/blob/master/lib/package/specification.fy](https://github.com/bakkdoor/fancy/blob/master/lib/package/specification.fy)
- [https://github.com/bakkdoor/fancy/blob/master/lib/package/dependency_installer.fy](https://github.com/bakkdoor/fancy/blob/master/lib/package/dependency_installer.fy)
