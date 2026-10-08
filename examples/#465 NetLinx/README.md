# #465 NetLinx

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire il codice startup NetLinx che scrive Hello, World! sul canale diagnostico0.

PROGRAM_NAME e DEFINE_START definiscono il programma. SEND_STRING0 usa una string expression NetLinx con il valore del saluto.

## Toolchain e riproduzione

AMX NetLinx Studio/compiler e controller o runtime compatibile; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Compilare hello.axs ed eseguire DEFINE_START nel runtime NetLinx.
```

## Risultato atteso e stato

Canale diagnostico0 mostra Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compiler/runtime AMX non preparati; nessun controller o dispositivo collegato.

## Fonti primarie

- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.axs` | [hello.axs](hello.axs), [driver.axs](variants/axi-f70cf351/driver.axs) creato, verifiche pendenti |
| `.axi` | [hello.axi](variants/axi-f70cf351/hello.axi) creato, verifiche pendenti |
