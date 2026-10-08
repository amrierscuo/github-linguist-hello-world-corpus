# 0550 — PowerBuilder: `.srw`

Ruolo: Oggetto window PowerBuilder esportabile con title del saluto e open MessageBox.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Appeon PowerBuilder originale; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
PowerBuilder: importare w_hello.srw in libreria di test e Open(w_hello) da application
```

Risultato atteso: Titolo e MessageBox Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `w_hello.srw`: `c31fd44de127e585c896a184ad44ed286f3b1827c91c488f6e38e401d8ad3722`

Fonti primarie:

- https://docs.appeon.com/pb2019r3/pbug/ch02s01.html
- https://www.appeon.com/system/files/product-manual/powerscript_reference_v2021.pdf
