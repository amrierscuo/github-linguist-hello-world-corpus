# #773 Windows Registry Entries

Voce canonica `Windows Registry Entries`, tipo `data`, language_id `969674868`.

File di importazione Windows Registry originale, con valore Message = `Hello, World!` sotto HKCU\Software\CorpusGreeting.

## Toolchain e riproduzione

Windows .reg import parser in disposable Windows registry hive — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

La struttura segue il formato REGEDIT5 documentato da Microsoft. Il file usa solo caratteri ASCII. Per una verifica nativa occorre un ambiente Windows usa e getta o un hive isolato supportato dal tool.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Solo in una VM Windows usa e getta: reg import hello.reg; reg query HKCU\Software\CorpusGreeting /v Message
```

Risultato atteso: Importazione riuscita e valore Message uguale a Hello, World! nell’ambiente usa e getta.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il log contiene soltanto il probe reg /?; tale comando non interpreta il sorgente e non attesta sintassi o semantica. L’importazione non è stata eseguita sul registro corrente.

Requisiti residui:

- Importazione nativa richiede un hive Windows usa e getta; nessuna modifica al registro corrente eseguita.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23](https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23)
- [https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.reg` | [hello.reg](hello.reg) creato, verifiche pendenti |
