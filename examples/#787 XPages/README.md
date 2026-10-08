# #787 XPages

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Caricare un controllo custom XPages configurato per mostrare Hello, World!.

L’artefatto canonico .xsp-config registra il controllo, namespace, tag e file composito. La fixture .xsp contiene il valore da renderizzare. Non si attribuisce una verifica XPages alla sola buona formazione XML.

## Toolchain e riproduzione

HCL Domino Designer/XPages, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Domino Designer: importare Greeting.xsp-config e Greeting.xsp nella cartella CustomControls, compilare e inserire il controllo Greeting in una pagina di prova
```

## Risultato atteso e stato

Controllo Greeting renderizzato con Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Domino Designer/XPages non disponibile; parser del componente e rendering pendenti.

## Fonti primarie

- https://help.hcl-software.com/dom_designer/10.0.1/basic/H_CUSTOM_CONTROLS_IN_ECLIPSE.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xsp-config` | [Greeting.xsp-config](Greeting.xsp-config) creato, verifiche pendenti |
| `.xsp.metadata` | artefatto da generare Designer XPages metadata con schema/versione proprietari non identificati: manca una struttura attendibile per questo suffisso composto e non viene rinominato il control .xsp. |
