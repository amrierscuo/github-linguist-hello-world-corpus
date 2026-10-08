# 0186 EdgeQL — variante `.esdl`

Ruolo: Schema ESDL con tipo Greeting e default della proprietà message, non query EdgeQL.

Tipo variante: **adapted**. Modello di partenza: examples/#186 EdgeQL/hello.edgeql; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Gel/EdgeDB in istanza temporanea: applicare lo schema hello.esdl; eseguire insert Greeting; select Greeting.message;
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

- [https://docs.geldata.com/reference/edgeql/select](https://docs.geldata.com/reference/edgeql/select)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.geldata.com/database/datamodel](https://docs.geldata.com/database/datamodel)
