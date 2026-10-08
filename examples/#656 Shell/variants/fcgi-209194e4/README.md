# 0656 — Shell — `.fcgi`

Entrypoint shell FastCGI che avvia l’adapter originale fcgiwrap; il companion CGI produce header/body. Non un echo rinominato.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.fcgi`.

Controllo previsto, dalla cartella della variante:

```text
spawn-fcgi -n -s /absolute/work/corpus-fcgi.sock -- sh hello.fcgi; isolated local FastCGI request SCRIPT_FILENAME=<absolute greeting.cgi>
```

Risultato atteso: FastCGI frontend riceve HTTP body Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://github.com/gnosek/fcgiwrap](https://github.com/gnosek/fcgiwrap)
- [https://www.rfc-editor.org/rfc/rfc3875](https://www.rfc-editor.org/rfc/rfc3875)
