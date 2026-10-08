# 0611 — Regular Expression — `.regex`

Variante testuale dello stesso formato, con suffisso canonico .regex.

Provenienza: copia del file originale `examples/#611 Regular Expression/hello.regexp`.

Artefatto principale: `hello.regex`.

Controllo previsto, dalla cartella della variante:

```text
python -c "import re,pathlib; r=re.compile(pathlib.Path('hello.regex').read_text().strip()); assert r.fullmatch('Hello, World!')"
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
