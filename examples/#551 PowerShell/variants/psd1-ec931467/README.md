# 0551 — PowerShell: `.psd1`

Ruolo: Manifest modulo PowerShell, hashtable di soli dati; RootModule è un fixture separato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: PowerShell7.6.5 originale Windows. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
pwsh -NoProfile -Command "Test-ModuleManifest ./hello.psd1; Import-Module ./hello.psd1; Get-CorpusGreeting"
```

Risultato atteso: Manifest accettato e Hello, World! dalla funzione

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `hello.psd1`: `c50399a95f7107c81eeeb8071bb1b890cf137543a25d09ccd07be62485824392`
- `hello.psm1`: `d22db22d41450b8c24a67bf19c2a5ff3b163c928d1344b899852a99f4ac0ca78`

Fonti primarie:

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_module_manifests
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output

Prova aggiuntiva realmente eseguita:

PowerShell originale: import del modulo; per .psd1 Test-ModuleManifest; funzione esportata eseguita e stdout esatto. Processo dedicato terminato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 7.6.5
