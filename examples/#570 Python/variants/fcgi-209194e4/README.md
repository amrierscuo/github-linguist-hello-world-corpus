# 0570 — Python — `.fcgi`

FastCGI process tramite il server originale flup; richiede un frontend locale FastCGI.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.fcgi`.

Controllo previsto, dalla cartella della variante:

```text
python hello.fcgi; frontend FastCGI local request
```

Risultato atteso: HTTP body Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.fastcgi.com/devkit/doc/fcgi-spec.html](https://www.fastcgi.com/devkit/doc/fcgi-spec.html)
- [https://pypi.org/project/flup6/](https://pypi.org/project/flup6/)
