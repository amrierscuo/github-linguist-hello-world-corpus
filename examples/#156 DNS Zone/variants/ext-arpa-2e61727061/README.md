# 0156 DNS Zone — variante `.arpa`

Ruolo: Zona DNS reverse IPv4 per il blocco documentale 192.0.2.0/24, con PTR e TXT saluto.

Tipo variante: **adapted**. Modello di partenza: examples/#156 DNS Zone/hello.zone; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
named-checkzone 2.0.192.in-addr.arpa hello.arpa; named-compilezone -D -o <output>/canonical.zone 2.0.192.in-addr.arpa hello.arpa
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

- [https://bind9.readthedocs.io/en/latest/manpages.html#named-checkzone-zone-file-validation-tool](https://bind9.readthedocs.io/en/latest/manpages.html#named-checkzone-zone-file-validation-tool)
- [https://www.isc.org/bind/](https://www.isc.org/bind/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://bind9.readthedocs.io/en/latest/reference.html](https://bind9.readthedocs.io/en/latest/reference.html)
