# #153 D2

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Renderizzare un nodo D2 la cui label è Hello, World!.

Il sorgente dichiara un nodo rectangle con una label. Il compilatore/renderer originale D2 interpreta il file e genera SVG; la label è testo effettivo dell’output XML. L’SVG generato non è incluso nel corpus.

## Toolchain e riproduzione

D2 0.9.0, distribuzione ufficiale Linux amd64

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
d2 hello.d2 hello.svg
```

```text
Controllare la label nell’SVG prodotto.
```

## Risultato atteso e stato

Il renderer termina exit 0 e l’SVG contiene il testo Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://d2lang.com/tour/hello-world/
- https://d2lang.com/tour/text/
- https://github.com/d2lang/d2/releases/tag/v0.9.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.d2` | [hello.d2](hello.d2) verificato |
