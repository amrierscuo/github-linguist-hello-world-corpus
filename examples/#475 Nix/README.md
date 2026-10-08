# #475 Nix

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Valutare un’espressione Nix e ottenere Hello, World!.

L’espressione pura let/in usa interpolazione ${audience}. Non contiene derivazioni, fetch o modifiche del sistema; la prova richiede comunque l’evaluator Nix.

## Toolchain e riproduzione

Nix evaluator originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nix-instantiate --eval --strict hello.nix
```

## Risultato atteso e stato

Valore stringa "Hello, World!".

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Nix originale non preparato; evaluator pendente.

## Fonti primarie

- https://nix.dev/manual/nix/stable/language/string-interpolation.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nix` | [hello.nix](hello.nix) creato, verifiche pendenti |
