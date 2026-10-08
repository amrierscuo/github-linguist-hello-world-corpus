# 0519 — PHP: `.inc`

Ruolo: Include PHP con funzione; driver richiede il file e stampa il valore.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: PHP 8.3.6 native Ubuntu CLI. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
php -l hello.inc; php driver.php
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.php`: `75283047904107e54ee5c21d5d203f3becc6ab4a5b2082eb88d96b1d11d92649`
- `hello.inc`: `7291d1b8718b1b36377f1dfc0023f57b75d9f5a76c7118e594f3c6fee9d65729`

Fonti primarie:

- https://www.php.net/manual/en/function.include.php
- https://www.php.net/manual/en/function.echo.php
