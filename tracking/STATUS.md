# Stato corrente del corpus

| Copertura | Stato |
| --- | ---: |
| Voci canoniche con artefatti o bozze | 836 / 836 |
| Voci con sintassi verificata per il campione principale | 534 / 836 |
| Voci con semantica verificata per il campione principale | 504 / 836 |
| Coppie linguaggio ed estensione con file | 1738 / 1749 |
| Estensioni distinte con artefatti principali | 1480 / 1489 |
| Coppie ancora senza artefatto | 11 |

Le 836 voci includono programmi, dati, markup e prosa. Le 1.749 coppie linguaggio ed estensione tengono distinti i suffissi condivisi.
Le estensioni non sono 836 linguaggi aggiuntivi e un linguaggio verificato non implica che tutte le sue varianti siano state verificate.

## I cinque casi completati come artefatti preliminari

- MiniD e Charity: snippet dell’utente conservati come bozze; grammatica e runtime non convalidati. Charity non è dichiarato programma funzionante.
- LabVIEW: modelli XML `.lvproj`, `.lvclass`, `.lvlib`; il VI grafico manca e deve essere creato nell’IDE.
- JetBrains MPS: campione ufficiale JetBrains adattato, con modello, linguaggio e soluzione; generazione ed esecuzione MPS pendenti. Licenza Apache-2.0 conservata.
- Altium Designer: quattro file ASCII originali accettati da altiumts0.0.89 con round-trip e asserzioni sul contenuto; import/riapertura in Altium e produzione Gerber pendenti.

## Consultazione

- [Tutte le estensioni e gli artefatti](EXTENSIONS.md).
- [Estensioni ancora senza artefatto](EXTENSIONS_PENDING.md).
- [Catalogo delle voci](CATALOG.md), [tracker dei linguaggi](languages_tracker.json), [tracker delle estensioni](extensions_tracker.json).
- [Contatori dei linguaggi](progress.json), [contatori delle estensioni](extensions_progress.json), [verifiche aggiuntive](RECHECKS.md).

I nuovi alias sono copie byte per byte dei sorgenti appropriati; le altre varianti hanno contenuti per il proprio ruolo (header, modulo, configurazione, descriptor o dati).
I formati non generati nativamente mantengono un impedimento e non vengono sostituiti con file vuoti o binari fittizi.
Le verifiche false restano false finché un parser, compilatore o consumatore reale non ha superato una prova registrata.

I comandi si trovano nei README. Toolchain, build e cache sono fuori dal corpus. I log conservano output/exit/timestamp e hashes effettivi; i prefissi locali sono normalizzati quando indicato.
La cattura in modalità testo può normalizzare CRLF in LF. Una modifica ai sorgenti verificati richiede una nuova prova.

Il riferimento YAML originale mantiene SHA-256 `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`.

Gli ZIP e i rapporti BATCH precedenti sono checkpoint storici; questa pagina e i tracker rappresentano lo stato corrente.
