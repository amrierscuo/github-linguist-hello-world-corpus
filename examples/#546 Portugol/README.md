# #546 Portugol

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire un programma Portugol2.0 e scrivere Hello, World!.

Il programma usa funcao inicio, cadeia e escreva con argomenti distinti. La forma è Portugol Studio, distinta da VisuAlg/Pascal.

## Toolchain e riproduzione

Portugol Studio/UNIVALI originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Aprire hello.por in Portugol Studio ed eseguire inicio.
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compiler/runtime Portugol Studio non preparati.

## Fonti primarie

- https://github.com/UNIVALI-LITE/Portugol-Studio
- https://univali-lite.github.io/Portugol-Studio/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.por` | [hello.por](hello.por) creato, verifiche pendenti |
