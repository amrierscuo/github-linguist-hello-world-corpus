# 0785 — XML — `.ps1xml`

PowerShell formatting data per stringhe; companion produce il saluto.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.ps1xml`.

Controllo previsto, dalla cartella della variante:

```text
PowerShell isolated process: Update-FormatData -PrependPath hello.ps1xml; run greet.ps1
```

Risultato atteso: XML ben formato che conserva il saluto; schema/importazione applicativa non verificati.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/powershell/scripting/developer/format/formatting-file-overview](https://learn.microsoft.com/en-us/powershell/scripting/developer/format/formatting-file-overview)
