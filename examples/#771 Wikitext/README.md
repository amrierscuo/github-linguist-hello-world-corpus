# #771 Wikitext

Voce canonica `Wikitext`, tipo `prose`, language_id `228`.

Pagina Wikitext originale con un titolo Greeting e il testo del saluto nel corpo.

## Toolchain e riproduzione

mwparserfromhell / Python 3.13.9 — 0.7.2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e mwparserfromhell 0.7.2 in ambiente isolato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Titolo Greeting, testo Hello, World! e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser Wikitext esistente costruisce l’AST; il driver controlla titolo e testo ottenuto da strip_code. L’obiettivo è la pagina sorgente e la sua vista testuale, senza affermare una resa HTML del server MediaWiki.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.mediawiki.org/wiki/Help:Formatting](https://www.mediawiki.org/wiki/Help:Formatting)
- [https://mwparserfromhell.readthedocs.io/en/latest/](https://mwparserfromhell.readthedocs.io/en/latest/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mediawiki` | [hello.mediawiki](hello.mediawiki) verificato |
| `.wiki` | [hello.wiki](variants/wiki-161d167f/hello.wiki) creato, verifiche pendenti |
| `.wikitext` | [hello.wikitext](variants/wikitext-b2a94597/hello.wikitext) creato, verifiche pendenti |
