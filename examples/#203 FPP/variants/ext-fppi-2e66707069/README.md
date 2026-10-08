# 0203 FPP — variante `.fppi`

Ruolo: Frammento FPP incluso all’interno di un modulo.

Tipo variante: **adapted**. Modello di partenza: examples/#203 FPP/hello.fpp; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
fpp-check consumer.fpp; fpp-to-xml -d <output> consumer.fpp; controllare constant Greeting.
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

- [https://nasa.github.io/fpp/fpp-spec.html](https://nasa.github.io/fpp/fpp-spec.html)
- [https://nasa.github.io/fpp/fpp-users-guide.html](https://nasa.github.io/fpp/fpp-users-guide.html)
- [https://github.com/nasa/fpp](https://github.com/nasa/fpp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://nasa.github.io/fpp/fpp-user-guide.html](https://nasa.github.io/fpp/fpp-user-guide.html)
