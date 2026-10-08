# 0068 BitBake — variante `.bbappend`

Ruolo: Append BitBake applicato al recipe hello_1.0.bb; estende la task Python.

Tipo variante: **adapted**. Modello di partenza: examples/#068 BitBake/meta-hello/classes/base.bbclass; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
In un layer BitBake temporaneo configurato: collocare hello_1.0.bb e hello_1.0.bbappend; bitbake hello -c build
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

- [https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html](https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html)
- [https://github.com/openembedded/bitbake/tree/2.10](https://github.com/openembedded/bitbake/tree/2.10)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.yoctoproject.org/bitbake/dev/bitbake-user-manual/bitbake-user-manual-metadata.html](https://docs.yoctoproject.org/bitbake/dev/bitbake-user-manual/bitbake-user-manual-metadata.html)
