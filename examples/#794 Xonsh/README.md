# #794 Xonsh

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire Xonsh e stampare Hello, World!.

Il parser/runtime Xonsh autentico esegue lo script. Il log conserva anche l’avviso sull’assenza di readline per uso interattivo; il saluto è la riga finale e la prova non usa una shell interattiva.

## Toolchain e riproduzione

Xonsh0.24.2 originale, Python3.13

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python -m xonsh --no-rc --shell-type dumb hello.xsh
```

## Risultato atteso e stato

Exit0 e riga finale Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://xon.sh/tutorial.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xsh` | [hello.xsh](hello.xsh) verificato |
