# 0170 Dotenv — variante `.env`

Ruolo: File dotenv; suffisso .env con gli stessi key/value del modello .env.example.

Tipo variante: **alias**. Copia byte-identica di examples/#170 Dotenv/.env.example

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
dotenv originale: dotenv.parse(readFileSync("hello.env")); verificare la proprietà greeting del modello.
```

Risultato atteso: Oggetto esattamente {GREETING:"Hello, World!"}; saluto stampato e exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/motdotla/dotenv#usage](https://github.com/motdotla/dotenv#usage)
- [https://github.com/motdotla/dotenv#parse](https://github.com/motdotla/dotenv#parse)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
