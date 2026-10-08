# 0016 ASN.1 — variante `.asn1`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#016 ASN.1/hello.asn

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
asn1tools compile -c uper hello.asn1; applicare lo stesso test encode/decode del modello al file variante.
```

Risultato atteso: DER 0c0b48656c6c6f20576f726c64; valore decodificato Hello World; PASS.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://asn1tools.readthedocs.io/en/latest/](https://asn1tools.readthedocs.io/en/latest/)
- [https://github.com/eerimoq/asn1tools](https://github.com/eerimoq/asn1tools)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
