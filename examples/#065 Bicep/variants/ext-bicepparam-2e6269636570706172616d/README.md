# 0065 Bicep — variante `.bicepparam`

Ruolo: File parametri Bicep, associato a un modulo con parametro dichiarato.

Tipo variante: **adapted**. Modello di partenza: examples/#065 Bicep/hello.bicep; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
bicep build-params hello.bicepparam --outfile <output>/parameters.json; bicep build main.bicep --outfile <output>/template.json
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

- [https://learn.microsoft.com/azure/azure-resource-manager/bicep/outputs](https://learn.microsoft.com/azure/azure-resource-manager/bicep/outputs)
- [https://github.com/Azure/bicep/releases](https://github.com/Azure/bicep/releases)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameter-files](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/parameter-files)
