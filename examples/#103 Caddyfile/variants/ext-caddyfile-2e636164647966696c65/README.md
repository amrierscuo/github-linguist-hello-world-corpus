# 0103 Caddyfile — variante `.caddyfile`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#103 Caddyfile/Caddyfile

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
caddy adapt --config hello.caddyfile --adapter caddyfile --validate
```

Risultato atteso: GET http://127.0.0.1:18763/ restituisce stato 200 e i 13 byte Hello, World!.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://caddyserver.com/docs/caddyfile/directives/respond](https://caddyserver.com/docs/caddyfile/directives/respond)
- [https://caddyserver.com/docs/command-line](https://caddyserver.com/docs/command-line)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
