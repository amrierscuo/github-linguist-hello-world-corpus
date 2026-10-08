# 0440 — Modula-3: `.ig`

Ruolo: Modula-3 generico: parametro formale di interfaccia T e istanziazione con Text; non semplice modulo .m3.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Critical Mass Modula-3 cm3 e libm3. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
cm3 con m3makefile del fixture; ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `Greeting.ig`: `7cd1246d92461256f6b4b256a7829a3e8a2a13085e07bc8e284a4a5539b36b25`
- `Greeting.mg`: `d8ccfec665689d926b0877ab34c79092148f18369b824dd0b9168a515e0fd117`
- `Main.m3`: `90299d575bd37e7dd629c4bca9aa8ca566a115c633c742fe14d61b1efe9e5e86`
- `TextGreeting.i3`: `714270937ae73c8195cf4dcfaf070130ac12737c2bc99fbcf37c7609b5ce16ee`
- `TextGreeting.m3`: `79bc59da58195e2238a75456e78e2471196cb542e921b460361779901d73ef33`
- `m3makefile`: `813bd87cb8c5e3db7f5d0a923fec3ce654f7954c21f709dceadd6b48492b94a1`

Fonti primarie:

- https://www.cs.purdue.edu/homes/hosking/m3/reference/complete/m3-defn-complete.pdf
- https://github.com/modula3/cm3
