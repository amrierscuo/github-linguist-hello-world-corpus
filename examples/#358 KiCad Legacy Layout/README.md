# #358 KiCad Legacy Layout

Voce canonica `KiCad Legacy Layout`, tipo `data`, language_id `140848857`.

Descrivere nel formato legacy KiCad .brd un testo di serigrafia Hello, World!.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Formato PCBNEW-BOARD Version 1, coordinate in 1/10000 inch. Il testo è un oggetto $TEXTPCB sul layer legacy 21; il file termina con $EndBOARD.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
PCB Editor KiCad: aprire/importare hello.brd in una copia di lavoro, salvare come .kicad_pcb ed esportare SVG della serigrafia frontale
```

Risultato atteso: Importazione nativa riuscita; serigrafia frontale mostra Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Questo è il formato legacy, distinto dall’artefatto S-expression moderno. Il saluto è il campo Te del vero oggetto testuale. Importatore/renderer KiCad assenti; i flag restano false.

Requisiti residui:

- Native KiCad legacy PCB importer/renderer is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://dev-docs.kicad.org/en/file-formats/legacy-pcb/](https://dev-docs.kicad.org/en/file-formats/legacy-pcb/)
- [https://docs.kicad.org/9.0/en/kicad/kicad.html](https://docs.kicad.org/9.0/en/kicad/kicad.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.brd` | [hello.brd](hello.brd) creato, verifiche pendenti |
