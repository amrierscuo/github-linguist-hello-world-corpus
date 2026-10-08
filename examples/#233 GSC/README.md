# #233 GSC

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare uno script GSC IW5 PC che chiama println con Hello, World!.

Questa voce usa il dialetto Game Script del motore IW, identificato dal compiler originale community. Il sorgente è scritto da zero, senza asset o dump di gioco. La prova nativa compila il file e conserva l’hash del bytecode in work; il motore di gioco non è avviato.

## Toolchain e riproduzione

xensik GSC Tool 1.5.1.359, distribuzione Windows x64

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
gsc-tool -m comp -g iw5 -s pc hello.gsc
```

```text
Con un motore IW5 PC compatibile, caricare lo script e chiamare main().
```

## Risultato atteso e stato

Bytecode hello.gscbin generato dal compiler; main stampa il saluto nel runtime di gioco.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Il runtime proprietario IW5 PC non è preparato; la chiamata println e l’esecuzione main restano pendenti.

## Fonti primarie

- https://github.com/xensik/gsc-tool
- https://github.com/xensik/gsc-tool/releases/tag/1.5.1

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gsc` | [hello.gsc](hello.gsc) sintassi verificata |
| `.csc` | [hello.csc](variants/ext-csc-2e637363/hello.csc) creato, verifiche pendenti |
| `.gsh` | [hello.gsh](variants/ext-gsh-2e677368/hello.gsh) creato, verifiche pendenti |
