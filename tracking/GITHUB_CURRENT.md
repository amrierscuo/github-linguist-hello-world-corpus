# GitHub Languages dopo il consolidamento

Misura API del 2026-10-08T23:44:23.740038+00:00, dopo il commit sorgente `96683b28b8186a849b46e34715f9381ff153aea4`. Repository privata, GitHub Pages disabilitato, loghi esclusi.

| Misura | Risultato |
| --- | ---: |
| Linguaggi rilevati | 574 |
| Byte riconosciuti | 273905 |
| Byte Lean | 13966 |
| Quota Lean | 5.09885% |

I cinque nomi aggiunti sono BASIC, MiniScript, PicoLisp, StringTemplate e Teal. I campioni sono stati resi distinguibili con costrutti o commenti validi del linguaggio e poi rieseguiti nei runtime originali. Non sono state aggiunte etichette `linguist-language`. Il file Objective-J `.sj` è inoltre prodotto dal serializer originale. Script di controllo, log e metadata sono esclusi dalle statistiche.

[Risposta API completa](github_languages_current.json). La misura precedente era 569 nomi; la barra compatta di GitHub può mostrare una parte dei nomi sotto Other. Le percentuali sono basate sui byte e possono cambiare con ulteriori sorgenti o nuove versioni di Linguist.

## I quattro gruppi ancora non rilevati

- B4X: il modulo B4J esiste, ma manca l’export originale con metadata che distingue il suffisso ambiguo `.bas`. Il runtime B4J non è stato verificato; il sorgente resta invariato.
- ArkTS, Bend e LLVM TableGen: presenti nello snapshot canonico ricevuto, assenti nella release Linguist v9.7.0. Questa differenza è compatibile con un ritardo della versione utilizzata da GitHub. La versione effettivamente distribuita da GitHub non è stata accertata: si tratta di un’inferenza, non di una garanzia di aggiornamento futuro.

Il riferimento comprende 578 gruppi teorici programming/markup. I tipi data e prose mantengono il comportamento predefinito. Non si raggiungono 836 nomi nella barra trasformando formati di dati in programmi o duplicando etichette.

## Fonti primarie

- [Linguist v9.7.0](https://github.com/github-linguist/linguist/releases/tag/v9.7.0)
- [Linguaggi della release](https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/languages.yml)
- [Euristiche della release](https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml)
- [Attributi Linguist](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md)
