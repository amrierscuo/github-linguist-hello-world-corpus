# 0033 ApacheConf — variante `.vhost`

Ruolo: Configurazione Apache: il suffisso varia, le direttive e il profilo standalone del modello rimangono identici.

Tipo variante: **alias**. Copia byte-identica di examples/#033 ApacheConf/httpd.conf

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
httpd -t -f <percorso-assoluto>/hello.vhost; avviare l’istanza isolata e leggere hello.txt con richiesta loopback.
```

Risultato atteso: Syntax OK ed exit 0; richiesta HTTP riuscita con corpo esattamente Hello, World! seguito da newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://httpd.apache.org/docs/2.4/programs/httpd.html](https://httpd.apache.org/docs/2.4/programs/httpd.html)
- [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/core.html)
- [https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
