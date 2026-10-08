# #371 LTspice Symbol

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Aprire un simbolo LTspice originale e visualizzare il valore Hello, World!.

L’artefatto è un simbolo grafico testuale .asy con finestra3 per Value. Il saluto è una label: questa fixture non definisce un modello elettrico e non viene simulata.

## Toolchain e riproduzione

Editor simboli LTspice originale; versione da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Aprire hello.asy nell’editor simboli LTspice.
```

## Risultato atteso e stato

Rettangolo, due pin e attributo Value visibile: Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: LTspice non preparato; parsing e visualizzazione nativi pendenti.

## Fonti primarie

- https://ez.analog.com/other-products/a/documents/DO22731/symbol-file-ad8611-asy-for-ltspice
- https://www.analog.com/en/resources/technical-articles/ltspice-how-to-import-third-party-models.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asy` | [hello.asy](hello.asy) creato, verifiche pendenti |
