# 0519 — PHP: `.ctp`

Ruolo: Template CakePHP storico .ctp con output HTML del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: PHP 8.3.6 native Ubuntu CLI. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
CakePHP 3: renderizzare hello.ctp con helper globale h disponibile
```

Risultato atteso: <p>Hello, World!</p>

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.ctp`: `7a44a503c8c2624438747d21638c303f9d76de794e05e97acacd79f0ac3d2d5c`

Fonti primarie:

- https://book.cakephp.org/3/en/views.html
- https://www.php.net/manual/en/function.echo.php
