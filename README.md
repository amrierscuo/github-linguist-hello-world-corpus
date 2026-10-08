# GitHub Linguist Hello World Corpus

Repository privato di prova per osservare le statistiche Languages di GitHub sugli esempi del corpus.

836 voci canoniche, numerate nello stesso ordine dello snapshot originale `reference/languages.yml`. I nomi delle cartelle vanno da `#001 1C Enterprise` a `#836 xBase`.

SHA-256 del riferimento: `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`.

| Copertura | Stato |
| --- | ---: |
| Voci con artefatti o bozze | 836 / 836 |
| Sintassi verificata dei campioni principali | 518 / 836 |
| Semantica verificata dei campioni principali | 468 / 836 |
| Coppie linguaggio ed estensione con file | 1737 / 1749 |

Gli stati distinguono bozze, file creati e programmi verificati. I byte degli esempi, dei log e del riferimento sono conservati dal corpus locale.

## Obiettivo Languages

Le 836 voci comprendono 563 programming, 71 markup, 184 data e 18 prose. Linguist conta normalmente programming e markup: 634 voci candidate, aggregate in 578 gruppi possibili nello snapshot. Il riconoscimento effettivo va misurato sul repository.

La barra compatta raggruppa parte dei linguaggi in `Other`. Le percentuali dipendono dai byte riconosciuti. `.gitattributes` identifica i campioni in `examples/` come codice del repository, superando l’esclusione predefinita di quella cartella come documentazione. README, tracker, log e script di verifica restano esclusi; i tipi data e prose mantengono il comportamento predefinito.

[Candidati alle statistiche](tracking/GITHUB_STATS.md) · [Stato dei programmi](tracking/STATUS.md) · [Estensioni](tracking/EXTENSIONS.md)

## Esportazione senza loghi

I loghi reperiti, le icone delle cartelle Windows e il catalogo HTML con tali immagini sono esclusi dal repository. La copia locale completa e gli ZIP precedenti li conservano. Le immagini che costituiscono campioni originali di un formato o risorse minime degli esempi restano parte degli esempi.

Non è attiva una pubblicazione GitHub Pages. Questo repository è una prova privata del rilevamento Languages.

## Audit locale

```sh
python tools/corpus.py audit
python tools/extension_coverage.py audit
```

Gli audit controllano integrità, contatori e prove registrate. Per eseguire un campione seguire il README della sua cartella; gli audit non rieseguono tutte le toolchain.

## Licenze e provenienza

La licenza MIT del riferimento GitHub Linguist è in `LICENSES/GitHub-Linguist-MIT.txt`. Gli adattamenti di terzi conservano le rispettive licenze e attribuzioni nelle proprie cartelle. Non è stata scelta una licenza generale per il nuovo materiale del corpus. La pubblicazione pubblica richiederà una revisione separata.

Il progetto è indipendente da GitHub e dagli autori dei linguaggi. Il commit e la data upstream dello snapshot ricevuto non sono noti; l’identità del riferimento è fissata dall’impronta.

## Esperimento Lean

GitHub ha rilevato 569 linguaggi dopo aver incluso i campioni `examples/` nelle statistiche. Il [campione aggiuntivo Lean](experiments/lean-share/README.md), verificato con Lean 4.0.0, ha portato la quota a **5,11%** dei byte riconosciuti. L’API continua a rilevare **569 linguaggi**. Gli esempi canonici e i contatori delle loro verifiche restano invariati.
