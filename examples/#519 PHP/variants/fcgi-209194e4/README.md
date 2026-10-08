# 0519 — PHP: `.fcgi`

Ruolo: Entrypoint PHP CGI/FastCGI con shebang, non daemon inventato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: PHP 8.3.6 native Ubuntu CLI. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
php-cgi -l hello.fcgi; PHP-CGI FastCGI host locale con richiesta loopback di test
```

Risultato atteso: Header text/plain e corpo Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.fcgi`: `c6a4b920b54e61085a64bd51bd914fd3fd659b3779ae490b667342d3ff2a344f`

Fonti primarie:

- https://www.php.net/manual/en/install.fpm.php
- https://www.php.net/manual/en/function.echo.php
