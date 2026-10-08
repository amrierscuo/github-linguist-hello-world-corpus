# #239 Genie

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare Genie attraverso il frontend Vala ed eseguire il programma nativo Hello, World!.

init è il punto di ingresso Genie; [indent=4] dichiara l’indentazione e print aggiunge newline. La prova effettiva usa valac -C con vapi isolati, poi GCC con gli header GLib isolati e le librerie WSL. Il C generato e il binario restano in work.

## Toolchain e riproduzione

Vala/Genie 0.56.16, GNU C 13.3.0 e GLib 2.80.0

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
valac hello.gs -o hello
```

```text
./hello
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://wiki.gnome.org/Projects/Genie
- https://gnome.pages.gitlab.gnome.org/vala/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gs` | [hello.gs](hello.gs) verificato |
