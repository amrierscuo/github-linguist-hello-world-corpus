# 0570 — Python — `.rpy`

Risorsa .rpy del web server Twisted, non un copione Ren’Py.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.rpy`.

Controllo previsto, dalla cartella della variante:

```text
twistd web --path .; GET /hello.rpy from localhost
```

Risultato atteso: HTTP body Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.twisted.org/en/stable/web/howto/using-twistedweb.html](https://docs.twisted.org/en/stable/web/howto/using-twistedweb.html)
