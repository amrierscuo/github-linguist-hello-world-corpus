# 0460 — NSIS: `.nsh`

Ruolo: Header NSIS con macro di messaggio, include guard e script driver.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Official NSIS script compiler and native Windows installer generator — v3.09-4. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
makensis driver.nsi; eseguire solo installer di test e leggere dettagli
```

Risultato atteso: Hello, World! nei dettagli

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.nsi`: `8ef590162df9e0ccb9ea1aca74bd3ab27f6ac49ce0b9d192fc394b34dcfea864`
- `hello.nsh`: `f728ae2ec188854dd45cc317be82c9a72d33a4903bd8a5bea99e0dee916d24b5`

Fonti primarie:

- https://nsis.sourceforge.io/Docs/Chapter5.html
- https://nsis.sourceforge.io/Docs/Chapter4.html
- https://nsis.sourceforge.io/Docs/
