# GitHub Linguist Hello World Corpus

[Apri il Linguist Dex](https://amrierscuo.github.io/github-linguist-hello-world-corpus/)

Una collezione di esempi e prove registrate per esplorare GitHub Linguist. La dashboard mostra **578 nomi**, numerati da **#001 a #578**, con i colori dei linguaggi, ricerca e schede consultabili anche da telefono.

L'ultima osservazione registrata rileva **575 nomi su GitHub**. ArkTS, Bend e LLVM TableGen hanno un marker dedicato: sono presenti nel riferimento, ma il loro nome non compare ancora nelle statistiche osservate. I numeri descrivono questo snapshot e questa osservazione, non un limite permanente di GitHub.

## Corpus e riproducibilità

Il corpus conserva **836 voci canoniche**, nello stesso ordine dello snapshot originale `reference/languages.yml`. Le cartelle vanno da `#001 1C Enterprise` a `#836 xBase`. La numerazione della dashboard è distinta da quella delle cartelle e dagli ID di Linguist.

SHA-256 del riferimento: `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`.

Il riferimento contiene 563 voci programming, 71 markup, 184 data e 18 prose. Le 634 voci programming e markup si aggregano in 578 nomi attraverso i gruppi di Linguist. La dashboard presenta questi nomi; i dati sulle estensioni restano nei tracker.

| Copertura registrata | Stato |
| --- | ---: |
| Voci con artefatti o bozze | 836 / 836 |
| Sintassi verificata dei campioni principali | 534 / 836 |
| Semantica verificata dei campioni principali | 504 / 836 |
| Coppie linguaggio ed estensione con file | 1738 / 1749 |

Ultimo consolidamento del corpus: **2026-10-09**. Gli stati distinguono bozze, file creati e programmi verificati. I comandi, gli output e gli hash delle prove sono conservati; gli audit controllano l'integrità registrata e non rieseguono tutte le toolchain. Per riprodurre un risultato seguire il README e i comandi del singolo esempio.

[Stato dei programmi](tracking/STATUS.md), [prove della ripresa](tracking/RESUME_20261009.md), [estensioni](tracking/EXTENSIONS.md), [statistiche GitHub](tracking/GITHUB_CURRENT.md).

## Per persone e agenti

Leggere [AGENTS.md](AGENTS.md) e la [guida operativa](docs/AGENT_GUIDE.md). L'[indice JSON](tracking/agent_index.json) permette di trovare percorsi, toolchain, comandi, prove e blocchi senza dipendere dall'indicizzazione GitHub.

```sh
python tools/query_corpus.py APL --json
python tools/query_corpus.py --extension .h --json
python tools/query_corpus.py --type programming --status pending --json
python tools/query_corpus.py --check-index
python tools/corpus.py audit
python tools/extension_coverage.py audit
```

La ricerca stampa informazioni e comandi senza eseguirli. Una verifica del campione principale non certifica ogni variante di estensione.

## Dashboard e GitHub Languages

GitHub Pages pubblica la cartella `site/` tramite il [workflow dedicato](.github/workflows/pages.yml). La dashboard è statica, senza tracciamento, font esterni o dipendenze da installare. Le animazioni rispettano la preferenza di movimento ridotto.

Le statistiche Languages contano i byte riconosciuti degli esempi. Dashboard, documentazione, tracker, log e strumenti di supporto restano esclusi tramite `.gitattributes`. I tipi data e prose mantengono il comportamento predefinito. Il [campione aggiuntivo Lean](experiments/lean-share/README.md) conserva l'esperimento richiesto del 5% e rimane separato dalle 836 voci canoniche.

## Licenza e attribuzioni

Il materiale originale del progetto è distribuito con [licenza MIT](LICENSE). Il [documento sul suo ambito](docs/LICENSING.md) distingue materiali originali, importazioni e marchi. Il riferimento Linguist conserva la sua licenza MIT; gli adattamenti di terzi mantengono licenze e attribuzioni nelle rispettive cartelle.

La dashboard include solo **16 loghi originali con permessi documentati**, ciascuno con le proprie condizioni, fonte e attribuzione nella [pagina dedicata](https://amrierscuo.github.io/github-linguist-hello-world-corpus/attributions.html). Gli altri loghi reperiti e le icone Windows restano in locale. La licenza MIT del progetto non copre loghi, marchi o materiale di terzi.

Progetto indipendente da GitHub e dagli autori dei linguaggi. La presenza di un marchio non implica affiliazione o approvazione.
