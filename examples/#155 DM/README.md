# #155 DM

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Compilare un mondo BYOND DM che scrive Hello, World! nel server log e si arresta.

hello.dm ridefinisce /world/New(), richiama ..() e usa l’output del mondo. hello.dme include il sorgente per DreamMaker. Il goal è un avvio server locale breve, senza mappe, client o risorse grafiche.

## Toolchain e riproduzione

BYOND DreamMaker e DreamDaemon; versioni effettive da registrare

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
DreamMaker hello.dme
```

```text
DreamDaemon hello.dmb -trusted -close
```

## Risultato atteso e stato

world.log mostra Hello, World! durante /world/New(); shutdown() conclude il mondo.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; parser/compilatore/runtime nativo non è stato eseguito per questa voce.

Impedimenti: Toolchain BYOND non preparata; compilazione DM e runtime DreamDaemon restano da eseguire.

## Fonti primarie

- https://www.byond.com/docs/guide/chap08.html
- https://www.byond.com/docs/ref/contents.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dm` | [hello.dm](hello.dm) creato, verifiche pendenti |
