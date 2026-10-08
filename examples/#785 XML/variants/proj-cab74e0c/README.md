# 0785 — XML — `.proj`

Fixture MSBuild XML con PropertyGroup e Target; estensione .proj conserva il ruolo di project/import/profile. Non dichiara SDK/deployment/compiler vendor configurati.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.proj`.

Controllo previsto, dalla cartella della variante:

```text
MSBuild hello.proj /t:Greeting (process/project isolato)
```

Risultato atteso: XML ben formato che conserva il saluto; schema/importazione applicativa non verificati.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-project-file-schema-reference](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-project-file-schema-reference)
