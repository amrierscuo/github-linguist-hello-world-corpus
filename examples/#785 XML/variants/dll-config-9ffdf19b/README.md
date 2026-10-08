# 0785 — XML — `.dll.config`

Config .NET di libreria/app con appSettings; nessun assembly fittizio.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.dll.config`.

Controllo previsto, dalla cartella della variante:

```text
System.Configuration mapped configuration read, isolated file
```

Risultato atteso: XML ben formato che conserva il saluto; schema/importazione applicativa non verificati.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/](https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/)
