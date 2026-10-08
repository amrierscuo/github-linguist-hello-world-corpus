# 0115 Checksums — variante `.md2`

Ruolo: Manifest checksum MD2 con digest reale dei byte della fixture originale; .sha2 sceglie SHA-256 e .sha3 sceglie SHA3-256 esplicitamente.

Tipo variante: **adapted**. Modello di partenza: examples/#115 Checksums/SHA256SUMS; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Checker MD2 compatibile con formato checksum GNU: verificare hello.md2.
```

Risultato atteso: Digest del payload corrispondente; greeting.txt OK.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities](https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/rhash/RHash](https://github.com/rhash/RHash)
- [https://www.pycryptodome.org/src/hash/md2](https://www.pycryptodome.org/src/hash/md2)
