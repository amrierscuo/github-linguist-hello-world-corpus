# #525 Papyrus

Voce canonica `Papyrus`, tipo `programming`, language_id `277`.

Emettere il saluto nel log Papyrus quando una quest originale riceve OnInit.

## Toolchain e riproduzione

Required genuine compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Creation Kit Papyrus compiler, script standard Quest/Debug e runtime Skyrim con logging attivo.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
PapyrusCompiler CorpusGreeting.psc -f=TESV_Papyrus_Flags.flg -i=/path/to/SkyrimScripts -o=build; collegare a una quest di prova e attivare OnInit nel gioco locale.
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale; compilatore e runtime host non disponibili. Evento e chiamata Debug.Trace sono eseguibili nel relativo host.

Requisiti residui:

- Required PapyrusCompiler compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://ck.uesp.net/wiki/Trace_-_Debug](https://ck.uesp.net/wiki/Trace_-_Debug)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.psc` | [CorpusGreeting.psc](CorpusGreeting.psc) creato, verifiche pendenti |
