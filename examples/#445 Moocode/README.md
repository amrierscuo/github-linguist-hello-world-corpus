# #445 Moocode

Voce canonica `Moocode`, tipo `programming`, language_id `237`.

Inviare il saluto al player tramite un corpo di verb Moocode.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede server LambdaMOO e database con player:tell, oltre a un player di prova autorizzato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
In un server LambdaMOO locale con database LambdaCore: creare un verb greeting sul player, caricare hello.moo con @program, quindi invocare player:greeting().
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Corpo di verb originale; server/database mancanti, compilazione ed esecuzione pending.

Requisiti residui:

- LambdaMOO-compatible server/database with a test verb and player is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.moo.mud.org/](https://www.moo.mud.org/)
- [https://github.com/wrog/lambdamoo](https://github.com/wrog/lambdamoo)
- [https://www.wrog.net/moo/pm1.8.1/ProgrammersManual.pdf](https://www.wrog.net/moo/pm1.8.1/ProgrammersManual.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.moo` | [hello.moo](hello.moo) creato, verifiche pendenti |
