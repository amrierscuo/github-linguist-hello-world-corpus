# 0032 Antlers — variante `.antlers.xml`

Ruolo: Vista Antlers con markup XML e interpolazione del dato greeting.

Tipo variante: **adapted**. Modello di partenza: examples/#032 Antlers/hello.antlers.html; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Statamic: renderizzare hello.antlers.xml come vista Antlers nel profilo compatibile, con greeting = "Hello, World!"; confrontare l’output.
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

- [https://statamic.dev/frontend/antlers](https://statamic.dev/frontend/antlers)
- [https://statamic.dev/getting-started/requirements](https://statamic.dev/getting-started/requirements)
- [https://github.com/statamic/cms/discussions/8696](https://github.com/statamic/cms/discussions/8696)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://statamic.dev/antlers](https://statamic.dev/antlers)
