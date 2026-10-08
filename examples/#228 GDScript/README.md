# #228 GDScript

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire un SceneTree GDScript che costruisce e stampa Hello, World!, poi termina.

_initialize è il punto di ingresso dello SceneTree. Il parser nativo controlla il file; lo stesso motore esegue la concatenazione, print e quit. Le prove headless non richiedono finestre o asset grafici.

## Toolchain e riproduzione

Godot Engine 4.7.2.stable.official.ed1daf0bf Windows x64

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
godot --headless --path . --check-only --script hello.gd
```

```text
godot --headless --path . --script hello.gd
```

## Risultato atteso e stato

Il banner Godot è seguito da Hello, World! e il processo termina exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html
- https://docs.godotengine.org/en/stable/classes/class_scenetree.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gd` | [hello.gd](hello.gd) verificato |
