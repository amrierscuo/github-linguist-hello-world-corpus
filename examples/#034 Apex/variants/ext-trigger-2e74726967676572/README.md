# 0034 Apex — variante `.trigger`

Ruolo: Trigger Apex prima dell’inserimento Account, con modifica del campo Description.

Tipo variante: **adapted**. Modello di partenza: examples/#034 Apex/hello.apex; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Parser/compiler Apex: compilare il trigger; solo in org di test autorizzata inserire Account e confrontare Description con Hello, World!.
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

- [https://github.com/apex-dev-tools/apex-parser](https://github.com/apex-dev-tools/apex-parser)
- [https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html](https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers.htm](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers.htm)
