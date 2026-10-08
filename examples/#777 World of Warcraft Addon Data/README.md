# #777 World of Warcraft Addon Data

Voce canonica `World of Warcraft Addon Data`, tipo `data`, language_id `396`.

Addon World of Warcraft originale: TOC Greeting.toc dichiara titolo e versione e carica Greeting.lua, che stampa `Hello, World!`.

## Toolchain e riproduzione

World of Warcraft native addon loader — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Il campo Interface 110200 dichiara un target retail 11.2.0, non una pretesa di compatibilità con ogni versione futura. Per altri client aggiornare esplicitamente quel target e verificare con il loader del client. Fonte: sorgenti UI originali Blizzard distribuiti nel mirror indicato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Nel client compatibile, collocare Greeting.toc e Greeting.lua in Interface/AddOns/Greeting; abilitare l’addon; ricaricare l’interfaccia e osservare il saluto nella chat.
```

Risultato atteso: Loader accetta Greeting.toc, carica Greeting.lua e compare Hello, World! nella chat.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Client e caricatore addon assenti. Il titolo TOC e lo script hanno uno scopo reale, ma una sola prova Lua non attesterebbe il caricamento TOC: entrambi i flag restano false.

Requisiti residui:

- Client World of Warcraft e caricatore addon assenti; metadata TOC e script sono creati, caricamento non provato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/Gethe/wow-ui-source](https://github.com/Gethe/wow-ui-source)
- [https://raw.githubusercontent.com/Gethe/wow-ui-source/live/Interface/AddOns/Blizzard_APIDocumentation/Blizzard_APIDocumentation.toc](https://raw.githubusercontent.com/Gethe/wow-ui-source/live/Interface/AddOns/Blizzard_APIDocumentation/Blizzard_APIDocumentation.toc)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.toc` | [Greeting.toc](Greeting.toc) creato, verifiche pendenti |
