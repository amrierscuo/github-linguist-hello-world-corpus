# 0519 — PHP: `.phpt`

Ruolo: Test PHPT originale con sezioni TEST/FILE/EXPECT, distinto da sorgente PHP rinominato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: PHP 8.3.6 native Ubuntu CLI. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
php /path/to/php-src/run-tests.php hello.phpt
```

Risultato atteso: PASS: output FILE coincide con EXPECT

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.phpt`: `5e9623fea97eb613fc1a3dd4dd20fbcd035482323e55f65a588cfdd7f642f849`

Fonti primarie:

- https://qa.php.net/phpt_details.php
- https://www.php.net/manual/en/function.echo.php
