# 0178 EJS — variante `.jst`

Ruolo: Template EJS/JST nello stesso sottoinsieme di interpolazione <%= greeting %>.

Tipo variante: **alias**. Copia byte-identica di examples/#178 EJS/hello.ejs

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
EJS originale: ejs.renderFile("hello.jst", {greeting:"Hello, World!"}); controllare h1.
```

Risultato atteso: HTML esattamente <h1>Hello, World!</h1> più newline; <world> viene escaped correttamente.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://ejs.co/#docs](https://ejs.co/#docs)
- [https://github.com/mde/ejs](https://github.com/mde/ejs)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
