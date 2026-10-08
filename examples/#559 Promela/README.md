# #559 Promela

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Simulare un processo init Promela e stampare Hello, World!.

Il modello usa init e printf. Spin originale analizza ed esegue il modello nella simulazione locale; la prova non attribuisce proprietà di model checking ulteriori al saluto.

## Toolchain e riproduzione

Spin6.5.2 ufficiale Ubuntu

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
spin -T hello.pml
```

## Risultato atteso e stato

Simulazione emette Hello, World!; un processo creato; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://spinroot.com/spin/Man/printf.html
- https://spinroot.com/spin/Man/promela.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pml` | [hello.pml](hello.pml) verificato |
