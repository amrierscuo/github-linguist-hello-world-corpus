# 0529 — Pascal: `.dfm`

Ruolo: Risorsa form Delphi in formato testuale con Caption del saluto, non Pascal.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Genuine Free Pascal compiler — 3.2.2. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Delphi: associare hello.dfm a unità TGreetingForm ereditata da TForm; aprire il form in progetto GUI locale
```

Risultato atteso: Titolo Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.dfm`: `61fd947682af5eeb4a1ab26bd2e3ce1eb65a853b453715df8d55ca1ead6047f2`

Fonti primarie:

- https://docwiki.embarcadero.com/RADStudio/en/Form_Files
- https://www.freepascal.org/docs.html
