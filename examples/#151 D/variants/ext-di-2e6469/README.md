# 0151 D — variante `.di`

Ruolo: Interface file D di con dichiarazione pubblica, implementazione e consumer separati.

Tipo variante: **adapted**. Modello di partenza: examples/#151 D/hello.d; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
ldc2 -betterC consumer.d greeting.d -of=<output>/hello; <output>/hello
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

- [https://dlang.org/spec/betterc.html](https://dlang.org/spec/betterc.html)
- [https://github.com/ldc-developers/ldc/releases/tag/v1.43.0](https://github.com/ldc-developers/ldc/releases/tag/v1.43.0)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://dlang.org/spec/d_interface.html](https://dlang.org/spec/d_interface.html)
