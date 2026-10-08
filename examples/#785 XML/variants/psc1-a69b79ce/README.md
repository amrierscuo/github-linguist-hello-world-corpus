# 0785 — XML — `.psc1`

PowerShell console descriptor senza snap-in; companion esegue il saluto nel processo di prova.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.psc1`.

Controllo previsto, dalla cartella della variante:

```text
powershell.exe -NoProfile -PSConsoleFile hello.psc1 -File greet.ps1
```

Risultato atteso: XML ben formato che conserva il saluto; schema/importazione applicativa non verificati.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
- [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/export-console](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/export-console)
