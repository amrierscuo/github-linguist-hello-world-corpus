# 0785 — XML — `.slnx`

Fixture Visual Studio solution XML con folder originale; nessun progetto esterno.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.slnx`.

Controllo previsto, dalla cartella della variante:

```text
dotnet sln hello.slnx list in an isolated folder
```

Risultato atteso: XML ben formato che conserva il saluto; schema/importazione applicativa non verificati.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln)
