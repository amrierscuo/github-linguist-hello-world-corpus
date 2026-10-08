# 0551 — PowerShell: `.psm1`

Ruolo: Modulo PowerShell con funzione pubblica; Export-ModuleMember evita main top-level.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: PowerShell7.6.5 originale Windows. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
pwsh -NoProfile -Command "Import-Module ./hello.psm1; Get-CorpusGreeting"
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `hello.psm1`: `363ba5e1c6cbede4bcf7e700f92b7472b39c4b13e632d88bd020a2b76a57c78e`

Fonti primarie:

- https://learn.microsoft.com/en-us/powershell/scripting/developer/module/how-to-write-a-powershell-script-module
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-output

Prova aggiuntiva realmente eseguita:

PowerShell originale: import del modulo; per .psd1 Test-ModuleManifest; funzione esportata eseguita e stdout esatto. Processo dedicato terminato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 7.6.5
