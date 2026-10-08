# 0465 — NetLinx: `.axi`

Ruolo: Include NetLinx con funzione del saluto, driver .axs distinto dal programma principale.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: AMX NetLinx Studio/compiler e controller o runtime compatibile; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
NetLinx Studio: compilare driver.axs e usare controller/emulatore di test
```

Risultato atteso: Hello, World! nel log seriale locale

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.axs`: `d7f6df75a1927e6c9c3be0ca8b75a6fc288b03fb6b20a8e3f4513a677f445720`
- `hello.axi`: `659530a33cde8889dd81a15934209d09fee090ff23e22ef51174995ae668b5b2`

Fonti primarie:

- https://www.amx.com/en/site_elements/netlinx-programming-language-reference-guide
- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language
