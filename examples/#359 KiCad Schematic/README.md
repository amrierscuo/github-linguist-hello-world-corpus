# #359 KiCad Schematic

Voce canonica `KiCad Schematic`, tipo `data`, language_id `622447435`.

Descrivere uno schema KiCad senza circuiti con un oggetto text visibile contenente il saluto.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Formato nativo .kicad_sch versione 20230121 compatibile con KiCad 7. Il documento contiene UUID originali, foglio A4, lib_symbols vuoto e un oggetto text.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
kicad-cli sch export svg --output build/ hello.kicad_sch; aprire in Schematic Editor e controllare il testo
```

Risultato atteso: Schema caricato; SVG mostra Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

L’obiettivo è il testo dello schema, non ERC di un circuito. Senza loader/exporter KiCad non vengono attribuiti flag positivi a un parsing S-expression generico.

Requisiti residui:

- Native KiCad schematic loader/exporter is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/](https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/)
- [https://docs.kicad.org/7.0/en/eeschema/eeschema.html](https://docs.kicad.org/7.0/en/eeschema/eeschema.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kicad_sch` | [hello.kicad_sch](hello.kicad_sch) creato, verifiche pendenti |
| `.kicad_sym` | [hello.kicad_sym](variants/kicad-sym-fe143994/hello.kicad_sym) creato, verifiche pendenti |
| `.sch` | [hello.sch](variants/sch-5766dac2/hello.sch) creato, verifiche pendenti |
