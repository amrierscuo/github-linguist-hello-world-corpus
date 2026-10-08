# 0570 — Python — `.pyi`

Type stub Python: descrive la funzione, non ne esegue il corpo.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.pyi`.

Controllo previsto, dalla cartella della variante:

```text
mypy main.py --strict
```

Risultato atteso: interfaccia accettata e implementazione restituisce il saluto.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://typing.python.org/en/latest/spec/distributing.html#stub-files](https://typing.python.org/en/latest/spec/distributing.html#stub-files)
