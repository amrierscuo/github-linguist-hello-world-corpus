# #778 Wren

Voce canonica `Wren`, tipo `programming`, language_id `713580619`.

Programma Wren originale che interpola il nome World e scrive il saluto con System.print.

## Toolchain e riproduzione

Original Wren 0.4.0 C VM / GCC — gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Sorgenti ufficiali Wren 0.4.0 dalla release tagged; GCC 13.3.0. WREN e output sono directory esterne all’esempio. host.c è un piccolo host originale per l’API C Wren; tutta la VM e il parser provengono dal progetto originale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Linux: gcc -std=c99 -I<WREN>/src/include -I<WREN>/src/vm -I<WREN>/src/optional host.c <WREN>/src/vm/*.c <WREN>/src/optional/*.c -lm -o <output>/wrenhost
<output>/wrenhost hello.wren
```

Risultato atteso: Hello, World! seguito da newline; exit code 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Compilazione della VM ufficiale con i moduli optional originali, poi wrenInterpret sul sorgente .wren. Il codice di ritorno WREN_RESULT_SUCCESS e stdout sono verificati. Nessun interprete scritto ad hoc viene usato.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://wren.io/embedding/](https://wren.io/embedding/)
- [https://wren.io/interpolation.html](https://wren.io/interpolation.html)
- [https://github.com/wren-lang/wren/releases/tag/0.4.0](https://github.com/wren-lang/wren/releases/tag/0.4.0)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.wren` | [hello.wren](hello.wren) verificato |
