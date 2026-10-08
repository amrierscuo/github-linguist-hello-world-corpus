# 0305 — IRC log: `.irclog`

Ruolo: Trascrizione IRC testuale offline in formato timestamp/nickname; nessuna sessione o messaggio reale.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: WeeChat logger/backlog; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Aprire il transcript come testo UTF-8; verificare struttura [HH:MM:SS] <nick> messaggio
```

Risultato atteso: Una riga con nickname illustrativo e Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.irclog`: `edd45d668d6d4f44d6f6c3f38cd85528e56e258ef96554560ba9a1ff1ef1101c`

Fonti primarie:

- https://github.com/github-linguist/linguist/tree/main/samples/IRC%20log
- https://weechat.org/files/doc/devel/weechat_user.en.html
- https://github.com/weechat/weechat/tree/main/src/plugins/logger
