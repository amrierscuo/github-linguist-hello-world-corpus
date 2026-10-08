# 0233 GSC — variante `.gsh`

Ruolo: Include shared GSH con funzione di saluto senza entry point.

Tipo variante: **adapted**. Modello di partenza: examples/#233 GSC/hello.gsc; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gsc-tool originale: compilare hello.gsh per un target Call of Duty esplicito; collegare/invocare nel client o script consumer compatibile.
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

- [https://github.com/xensik/gsc-tool](https://github.com/xensik/gsc-tool)
- [https://github.com/xensik/gsc-tool/releases/tag/1.5.1](https://github.com/xensik/gsc-tool/releases/tag/1.5.1)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
