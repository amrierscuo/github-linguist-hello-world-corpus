# 0385 — Limbo: `.m`

Ruolo: Interfaccia di modulo Limbo: dichiarazioni pubbliche, nessun implement init.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Inferno/Limbo; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Limbo: includere draw.m e hello.m nel modulo hello.b, compilare con limbo e invocare init
```

Risultato atteso: Interfaccia del modulo Hello accettata; implementazione stampa Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Il fixture originale dichiara già Hello inline: sostituire quella dichiarazione con include "hello.m" nella directory di build, mantenendo il sorgente principale intatto.

SHA-256 dei file della variante:

- `hello.b`: `aad0676a4f4d15fc631c51c3543141e77763337b62eebf8763392a9650791c28`
- `hello.m`: `b7645ca6b02dd10fefd462bdaacf2cd1836c87189f8b510acb5425fbffb234d0`

Fonti primarie:

- https://inferno-os.org/inferno/limbo.html
- https://www.vitanuova.com/inferno/limbo.html
- https://www.vitanuova.com/inferno/papers/limbo.html
