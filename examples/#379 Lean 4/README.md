# #379 Lean 4

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Verificare il teorema greeting_length in Lean4 e stampare Hello, World!.

Usa String, IO Unit e il tactic decide di Lean4. La distribuzione4.0.0 viene tenuta distinta dal compiler3.51.1; il teorema e main sono verificati dal rispettivo ambiente originale.

## Toolchain e riproduzione

Lean4.0.0 ufficiale Linux

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

- https://lean-lang.org/documentation/
- https://github.com/leanprover/lean4/releases/tag/v4.0.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lean` | [hello.lean](hello.lean) verificato |
