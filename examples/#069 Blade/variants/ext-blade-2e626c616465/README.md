# 0069 Blade — variante `.blade`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#069 Blade/hello.blade.php

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Laravel Blade: renderizzare hello.blade con greeting = "Hello, World!" tramite il renderer Blade originale.
```

Risultato atteso: stdout esatto <p>Hello, World!</p> seguito da newline; exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://laravel.com/docs/12.x/blade](https://laravel.com/docs/12.x/blade)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
