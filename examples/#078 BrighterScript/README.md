# #078 BrighterScript

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Validare e transpilare un namespace BrighterScript, poi eseguire il BrightScript generato.

Corpus.greeting restituisce la stringa; main la stampa. bsconfig.json configura lo staging locale e disabilita la creazione di un pacchetto. La semantica è stata verificata con brs fuori da un dispositivo Roku.

## Toolchain e riproduzione

BrighterScript 0.73.5; brs 0.45.0; Node.js 22.20.0

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bsc --project bsconfig.json
```

```text
brs stage/source/main.brs
```

## Risultato atteso e stato

Validazione senza errori; stdout esatto Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://github.com/rokucommunity/brighterscript
- https://github.com/rokucommunity/brighterscript/blob/master/docs/bsconfig.md
- https://github.com/sjbarag/brs

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bs` | [main.bs](source/main.bs) verificato |
