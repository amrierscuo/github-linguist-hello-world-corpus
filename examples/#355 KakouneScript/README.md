# #355 KakouneScript

Voce canonica `KakouneScript`, tipo `programming`, language_id `603336474`.

Eseguire uno script Kakoune che scrive il saluto nel buffer debug e salvare quel risultato per confronto.

## Toolchain e riproduzione

Official Kakoune command parser and editor runtime — Kakoune unknown. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Kakoune dal pacchetto Ubuntu 2022.10.31-2. Il comando -version riporta "Kakoune unknown" nella build del pacchetto; la provenienza è documentata dall’archivio .deb. Il terminale dummy evita una UI interattiva.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
kak -n -ui dummy -e "source hello.kak; buffer '*debug*'; write build/debug.txt; quit!"
```

Risultato atteso: Debug buffer contiene Hello, World!; exit 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser/runtime reale carica il file .kak ed esegue echo -debug. Il buffer salvato contiene il saluto e il processo termina 0; il contenuto osservato è conservato nel log.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/mawww/kakoune/blob/master/doc/pages/commands.asciidoc](https://github.com/mawww/kakoune/blob/master/doc/pages/commands.asciidoc)
- [https://github.com/mawww/kakoune](https://github.com/mawww/kakoune)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kak` | [hello.kak](hello.kak) verificato |
