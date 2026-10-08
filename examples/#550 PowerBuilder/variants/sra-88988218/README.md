# 0550 — PowerBuilder: `.sra`

Ruolo: Oggetto application PowerBuilder esportabile, evento open mostra il saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Appeon PowerBuilder originale; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
PowerBuilder: importare corpus_hello.sra in libreria di test e impostare application target
```

Risultato atteso: MessageBox Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `corpus_hello.sra`: `d23ab37da300ef38690905e9198640b61f22f0402ed11965d556f548ab7a6c18`

Fonti primarie:

- https://docs.appeon.com/pb2019r3/pbug/ch02s01.html
- https://www.appeon.com/system/files/product-manual/powerscript_reference_v2021.pdf
