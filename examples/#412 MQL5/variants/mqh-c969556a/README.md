# 0412 — MQL5: `.mqh`

Ruolo: Header MQL con funzione di saluto e include guard; script driver separato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: MetaTrader 5 MetaEditor/compiler. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
MetaEditor: compilare driver.mq5; eseguire solo il driver nel terminale di test
```

Risultato atteso: Hello, World! nel log

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.mq5`: `15427813b05b8d56597fb04f22d728c2df82fa338dd90ea4e2247ea300beecc7`
- `hello.mqh`: `4bfd7b1c085b5be99e2ef9cd96d39efdf509667aaa07ac6486e86dcef421b0c6`

Fonti primarie:

- https://www.mql5.com/en/docs/basis/preprosessor/include
- https://www.mql5.com/en/docs/event_handlers/onstart
- https://www.mql5.com/en/docs/common/print
