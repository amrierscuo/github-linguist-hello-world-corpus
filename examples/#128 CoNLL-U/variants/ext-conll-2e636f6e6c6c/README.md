# 0128 CoNLL-U — variante `.conll`

Ruolo: Tabella CoNLL-X a 10 colonne (HEAD/DEPREL/PHEAD/PDEPREL), distinta dalle colonne DEPS/MISC CoNLL-U.

Tipo variante: **adapted**. Modello di partenza: examples/#128 CoNLL-U/hello.conllu; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Parser CoNLL-X: leggere hello.conll, verificare quattro token e dependency tree; ricomporre Hello, World!.
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

- [https://universaldependencies.org/format.html](https://universaldependencies.org/format.html)
- [https://github.com/UniversalDependencies/tools/tree/master/udtools](https://github.com/UniversalDependencies/tools/tree/master/udtools)
- [https://universaldependencies.org/u/dep/vocative.html](https://universaldependencies.org/u/dep/vocative.html)
- [https://github.com/EmilStenstrom/conllu](https://github.com/EmilStenstrom/conllu)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://ilk.uvt.nl/conll/](https://ilk.uvt.nl/conll/)
