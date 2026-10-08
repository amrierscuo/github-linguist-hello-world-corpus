# #357 KiCad Layout

Voce canonica `KiCad Layout`, tipo `data`, language_id `187`.

Descrivere una scheda KiCad con bordo rettangolare e testo Hello, World! sulla serigrafia frontale.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Formato nativo .kicad_pcb versione 20221018 compatibile con KiCad 7. Il file contiene due layer rame, serigrafia ed Edge.Cuts; nessun componente o routing è necessario per l’obiettivo.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
kicad-cli pcb export svg --layers F.Silkscreen,Edge.Cuts --output build/ hello.kicad_pcb; aprire la scheda in PCB Editor e controllare testo e bordo
```

Risultato atteso: KiCad carica la scheda e l’SVG mostra bordo rettangolare e Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il saluto è un vero gr_text visibile. La descrizione è originale e segue la documentazione del formato; la toolchain CAD non è disponibile e non viene sostituita da un generico parser S-expression.

Requisiti residui:

- Native KiCad PCB loader/exporter is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/](https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/)
- [https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html](https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kicad_pcb` | [hello.kicad_pcb](hello.kicad_pcb) creato, verifiche pendenti |
| `.kicad_mod` | [hello.kicad_mod](variants/kicad-mod-72f4d4f5/hello.kicad_mod) creato, verifiche pendenti |
| `.kicad_wks` | [hello.kicad_wks](variants/kicad-wks-ff39775a/hello.kicad_wks) creato, verifiche pendenti |
