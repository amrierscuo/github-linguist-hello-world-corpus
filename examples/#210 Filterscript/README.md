# #210 Filterscript

Voce canonica `Filterscript`, tipo `programming`, language_id `112`.

Descrivere un kernel Android FilterScript che scrive il carattere ASCII corrispondente a ciascun indice di una allocation U8 di tredici elementi.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede una toolchain Android storica con llvm-rs-cc e un runtime RenderScript/FilterScript compatibile. RenderScript è deprecato; la toolchain corrente qui non è configurata.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Progetto Android con SDK/Build Tools storici che supportano FilterScript: compilare hello.fs; invocare ScriptC_hello.forEach_root su allocation U8 lunga 13 e copiarne i byte sul lato Java
```

Risultato atteso: Kernel compilato; allocation ricostruita uguale a Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il kernel root ritorna valori ASCII reali per x=0..12. Non viene compilato come semplice C per attestare FilterScript; quel controllo ignorerebbe le restrizioni del linguaggio e il runtime.

Requisiti residui:

- Historical Android FilterScript compiler/SDK runtime and compatible device/emulator are unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://developer.android.com/guide/topics/renderscript/compute](https://developer.android.com/guide/topics/renderscript/compute)
- [https://source.android.com/docs/core/architecture/graphics/renderscript](https://source.android.com/docs/core/architecture/graphics/renderscript)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fs` | [hello.fs](hello.fs) creato, verifiche pendenti |
