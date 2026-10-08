# 0314 — Inno Setup: `.isl`

Ruolo: File messaggi Inno Setup: override localizzato del messaggio WelcomeLabel1.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Inno Setup ISCC; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
ISCC driver.iss; avviare l’installer solo in ambiente di test per leggere WelcomeLabel1
```

Risultato atteso: Il messaggio iniziale del wizard contiene Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.iss`: `27b0d587ceff68c99ddd4f95c40a3558eb94b63c82a00b098b9cff0ce483b7e7`
- `hello.isl`: `f7eed62fa011bddb6269cbbb42e0bfef5ddffedf20ae83d734d303a7207be7be`

Fonti primarie:

- https://jrsoftware.org/ishelp/topic_messagessection.htm
- https://jrsoftware.org/ishelp/topic_setupsection.htm
- https://jrsoftware.org/ishelp/topic_scriptevents.htm
- https://jrsoftware.org/ishelp/topic_isxfunc_msgbox.htm
