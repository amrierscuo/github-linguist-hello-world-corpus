# #378 Lean

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Verificare il tipo e la lunghezza del saluto in Lean3, poi stampare Hello, World!.

Importa system.io, usa string e io unit dell’API Lean3. La prova rfl e il programma sono elaborati dal compiler/kernel originale Lean3 prima dell’esecuzione.

## Toolchain e riproduzione

Lean3.51.1 community ufficiale Windows

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
lean hello.lean
```

```text
lean --run hello.lean
```

## Risultato atteso e stato

Il kernel accetta greeting.length=13; stdout Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://github.com/leanprover-community/lean/releases/tag/v3.51.1
- https://leanprover-community.github.io/lean3/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lean` | [hello.lean](hello.lean) verificato |
| `.hlean` | [hello.hlean](variants/hlean-a04be067/hello.hlean) creato, verifiche pendenti |
