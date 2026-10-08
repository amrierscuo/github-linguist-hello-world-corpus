# #077 Brainfuck

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Eseguire un programma Brainfuck originale che emette Hello, World! e newline.

Il programma usa una cella e variazioni aritmetiche tra i codici ASCII successivi. La verifica usa il parser e interprete nativo del progetto upstream; non usa un interprete scritto per questo corpus.

## Toolchain e riproduzione

fabianishere/brainfuck 2.7.3, interprete C originale compilato con GNU C

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
Compilare l’interprete upstream con la dipendenza opzionale editline disabilitata.
```

```text
brainfuck hello.bf
```

## Risultato atteso e stato

stdout esatto Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://github.com/fabianishere/brainfuck

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.b` | [hello.b](variants/ext-b-2e62/hello.b) creato, verifiche pendenti |
| `.bf` | [hello.bf](hello.bf) verificato |
