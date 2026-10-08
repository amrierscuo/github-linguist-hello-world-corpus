# 0798 — YARA — `.yara`

Variante testuale dello stesso formato, con suffisso canonico .yara.

Provenienza: copia del file originale `examples/#798 YARA/hello.yar`.

Artefatto principale: `hello.yara`.

Controllo previsto, dalla cartella della variante:

```text
yara hello.yara greeting.txt
```

Risultato atteso: Una corrispondenza CorpusGreeting per Hello, World!, nessuna per Hello, Moon!..

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://yara.readthedocs.io/en/stable/writingrules.html](https://yara.readthedocs.io/en/stable/writingrules.html)
