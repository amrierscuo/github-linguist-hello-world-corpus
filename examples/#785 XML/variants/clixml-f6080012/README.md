# 0785 — XML — `.clixml`

Serializzazione CLIXML di una stringa; parser/import originale ancora pendente.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.clixml`.

Controllo previsto, dalla cartella della variante:

```text
PowerShell Import-Clixml hello.clixml; assert returned string
```

Risultato atteso: XML ben formato che conserva il saluto; schema/importazione applicativa non verificati.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-clixml)
