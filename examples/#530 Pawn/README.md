# #530 Pawn

Voce canonica `Pawn`, tipo `programming`, language_id `271`.

Stampare il saluto tramite il console host della distribuzione Pawn originale.

## Toolchain e riproduzione

Required genuine compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede CompuPhase Pawn, console.inc e il runner host con le native console registrate.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
pawncc hello.pwn -obuild/hello.amx; pawnrun build/hello.amx
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Programma originale secondo il language guide; compiler/host non configurati.

Requisiti residui:

- Required pawncc compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://compuphase.com/pawn/pawn.htm](https://compuphase.com/pawn/pawn.htm)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pwn` | [hello.pwn](hello.pwn), [driver.pwn](variants/inc-dd126fb7/driver.pwn) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
| `.sma` | [hello.sma](variants/sma-3aced296/hello.sma) creato, verifiche pendenti |
