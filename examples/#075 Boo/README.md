# #075 Boo

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Eseguire una concatenazione e print in Boo.

Il sorgente usa la sintassi originale Boo e l’inferenza del tipo stringa. Non è convertito in Python; la verifica richiede booi autentico.

## Toolchain e riproduzione

Boo con booi e runtime .NET/Mono compatibile; versione effettiva da registrare

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
booi hello.boo
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; nessun parser o runtime nativo è stato eseguito per questa voce.

Impedimenti: Boo/booi e il suo runtime compatibile non disponibili; nessun compilatore Boo è stato eseguito.

## Fonti primarie

- https://github.com/boo-lang/boo
- https://boo-language.github.io/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.boo` | [hello.boo](hello.boo) creato, verifiche pendenti |
