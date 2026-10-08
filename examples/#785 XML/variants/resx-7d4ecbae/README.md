# 0785 — XML — `.resx`

Risorsa .NET RESX textuale, distinta da output binario .resources.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.resx`.

Controllo previsto, dalla cartella della variante:

```text
resgen hello.resx work/hello.resources or ResXResourceReader
```

Risultato atteso: risorsa Greeting == Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/dotnet/framework/resources/working-with-resx-files-programmatically](https://learn.microsoft.com/en-us/dotnet/framework/resources/working-with-resx-files-programmatically)
