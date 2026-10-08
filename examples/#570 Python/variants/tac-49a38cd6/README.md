# 0570 — Python — `.tac`

Descrittore Twisted application con endpoint limitato a loopback.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.tac`.

Controllo previsto, dalla cartella della variante:

```text
twistd --nodaemon --pidfile=work/hello.pid --logfile=work/hello.log -y hello.tac; local GET localhost:8080
```

Risultato atteso: HTTP body Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.twisted.org/en/stable/core/howto/application.html](https://docs.twisted.org/en/stable/core/howto/application.html)
