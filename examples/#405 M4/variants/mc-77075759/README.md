# 0405 — M4: `.mc`

Ruolo: Configurazione m4/sendmail: greeting in VERSIONID, non un main m4 rinominato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: GNU M4 extracted Ubuntu package. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Dalla distribuzione sendmail-cf: m4 hello.mc > hello.cf (offline; non avviare sendmail)
```

Risultato atteso: Configurazione sendmail testuale con VERSIONID del saluto

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mc`: `ac14cf978206c61aa6836be1be472547b2b93f3e26faa81debd8b5c24f141586`

Fonti primarie:

- https://www.sendmail.org/~ca/email/doc8.12/cf/m4/README
- https://www.gnu.org/software/m4/manual/m4.html
