# #232 GN

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Valutare una build GN e far produrre greeting.txt ad una vera action Ninja.

.gn seleziona il buildconfig originale e l’interprete Python per le action. BUILD.gn definisce un toolchain minimale con stamp e una action. hello.py è una fixture che scrive l’output richiesto. La verifica passa tramite GN e Ninja, non esegue la fixture da sola.

## Toolchain e riproduzione

GN 1000 (03d10f1), pacchetto Ubuntu generate-ninja; Ninja 1.11.1; Python 3.12.3

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
gn gen out
```

```text
ninja -C out greeting
```

## Risultato atteso e stato

Action reale produce out/gen/greeting.txt esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://gn.googlesource.com/gn/+/main/docs/quick_start.md
- https://gn.googlesource.com/gn/+/main/docs/reference.md
- https://ninja-build.org/manual.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gn` | [.gn](.gn), [BUILD.gn](BUILD.gn), [BUILDCONFIG.gn](BUILDCONFIG.gn) verificato |
| `.gni` | [hello.gni](variants/ext-gni-2e676e69/hello.gni) creato, verifiche pendenti |
