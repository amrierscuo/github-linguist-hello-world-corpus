# #201 FIRRTL

Voce canonica `FIRRTL`, tipo `programming`, language_id `906694254`.

Descrivere un circuito FIRRTL con tredici uscite ASCII che formano il saluto e un printf attivo quando reset è basso.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede CIRCT firtool e un simulatore RTL. Fornire clock e reset al modulo; i campioni greeting[0..12] devono ricostruire il saluto. La simulazione va fatta in una directory di lavoro.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
firtool hello.fir -o build/hello.sv; simulare il modulo Hello con clock e reset in un testbench RTL
```

Risultato atteso: Compilatore accetta il circuito; uscite ASCII e printf producono Hello, World! durante la simulazione.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il testo è un circuito originale, con vettore UInt<8>[13] e printf del linguaggio FIRRTL. Nessun compilatore/simulatore è disponibile; i soli byte presenti nel sorgente non sono una prova di esecuzione.

Requisiti residui:

- CIRCT firtool and RTL simulation are unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/chipsalliance/firrtl-spec](https://github.com/chipsalliance/firrtl-spec)
- [https://circt.llvm.org/docs/Dialects/FIRRTL/](https://circt.llvm.org/docs/Dialects/FIRRTL/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fir` | [hello.fir](hello.fir) creato, verifiche pendenti |
