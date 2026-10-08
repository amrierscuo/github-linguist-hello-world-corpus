# 0570 — Python — `.wsgi`

Applicazione WSGI conforme alla convenzione application; non è uno script print.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.wsgi`.

Controllo previsto, dalla cartella della variante:

```text
WSGI server: load application from hello.wsgi; local request only
```

Risultato atteso: HTTP 200 e body Hello, World! seguito da LF.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://peps.python.org/pep-3333/](https://peps.python.org/pep-3333/)
