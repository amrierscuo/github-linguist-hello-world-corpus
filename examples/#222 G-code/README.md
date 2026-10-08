# #222 G-code

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Definire il messaggio LCD Hello, World! mediante M117 nel dialetto Marlin, senza movimenti.

L’artefatto usa una sola istruzione M117 con testo libero. Il parser originale gcodeparser riconosce M117 ma tratta le lettere del messaggio come parametri: questa prova lessicale non convalida il dialetto completo. Nessun comando è stato inviato a macchine o porte seriali.

## Toolchain e riproduzione

Marlin M117; parser Python gcodeparser 0.3.0 provato offline

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Solo offline: analizzare hello.gcode con un parser che supporti il testo libero Marlin M117.
```

## Risultato atteso e stato

Il comando M117 ha il messaggio Hello, World!; non contiene istruzioni di movimento.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Il parser disponibile non supporta correttamente l’argomento testo libero M117; sintassi del dialetto e messaggio LCD restano non verificati.

## Fonti primarie

- https://marlinfw.org/docs/gcode/M117.html
- https://github.com/AndyEveritt/GcodeParser

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.g` | [hello.g](variants/ext-g-2e67/hello.g) creato, verifiche pendenti |
| `.cnc` | [hello.cnc](variants/ext-cnc-2e636e63/hello.cnc) creato, verifiche pendenti |
| `.gco` | [hello.gco](variants/ext-gco-2e67636f/hello.gco) creato, verifiche pendenti |
| `.gcode` | [hello.gcode](hello.gcode) creato, verifiche pendenti |
