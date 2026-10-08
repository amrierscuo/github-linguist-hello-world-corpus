# #555 Processing

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire uno sketch Processing originale e stampare Hello, World!.

La directory Hello contiene Hello.pde. setup dichiara una variabile String, chiama println e conclude lo sketch con exit; il preprocessing Processing è distinto da javac su un file C/Java generico.

## Toolchain e riproduzione

Processing Java mode originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
processing-java --sketch=Hello --run
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Processing/Java-mode preprocessor e host non preparati.

## Fonti primarie

- https://processing.org/reference/println_.html
- https://processing.org/reference/exit_.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pde` | [Hello.pde](Hello/Hello.pde) creato, verifiche pendenti |
