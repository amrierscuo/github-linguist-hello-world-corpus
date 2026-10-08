# #079 Brightscript

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Eseguire sub main e stampare Hello, World! nel linguaggio BrightScript.

La voce canonica Linguist è Brightscript. Il codice usa il linguaggio Roku BrightScript; la prova effettiva avviene tramite brs in Node, senza hardware o API di un dispositivo Roku.

## Toolchain e riproduzione

brs 0.45.0, interprete BrightScript originale della community; Node.js 22.20.0

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
brs hello.brs
```

## Risultato atteso e stato

stdout esatto Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://github.com/sjbarag/brs
- https://developer.roku.com/docs/references/brightscript/language/expressions-variables-types.md

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.brs` | [hello.brs](hello.brs) verificato |
