# #775 Wolfram Language

Voce canonica `Wolfram Language`, tipo `programming`, language_id `224`.

Espressioni Wolfram Language originali che assegnano il destinatario, compongono la stringa con StringJoin e la stampano con Print.

## Toolchain e riproduzione

Mathics3 (compatible Wolfram Language evaluator) — Mathics3 10.0.1; Running on win32 CPython 3.13.9 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 19:09:58) [MSC v.1929 64 bit (AMD64)]; using SymPy 1.14.0, mpmath 1.3.0, numpy 2.3.5, cython Not installed, scipy 1.16.3, skimage 0.25.2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e Mathics3 10.0.1, Mathics3-Scanner 10.0.1, SymPy 1.14.0; installare le dipendenze di Mathics3 in un ambiente isolato. Il driver inizializza i builtin e la sessione del motore originale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! dall’output Print e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il sorgente .wl è interpretato realmente da Mathics3, motore open source compatibile con questo sottoinsieme Wolfram Language. Il driver controlla l’output Print della sessione. Non viene dichiarata una verifica con Wolfram Kernel proprietario.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://reference.wolfram.com/language/ref/Print.html](https://reference.wolfram.com/language/ref/Print.html)
- [https://reference.wolfram.com/language/ref/StringJoin.html](https://reference.wolfram.com/language/ref/StringJoin.html)
- [https://mathics.org/](https://mathics.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mathematica` | [hello.mathematica](variants/mathematica-ce2c0b75/hello.mathematica) creato, verifiche pendenti |
| `.cdf` | [hello.cdf](variants/cdf-cfab4dd6/hello.cdf) creato, verifiche pendenti |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) creato, verifiche pendenti |
| `.ma` | [hello.ma](variants/ma-bf225f29/hello.ma) creato, verifiche pendenti |
| `.mt` | [hello.mt](variants/mt-d80ef8fe/hello.mt) creato, verifiche pendenti |
| `.nb` | [hello.nb](variants/nb-af372417/hello.nb) creato, verifiche pendenti |
| `.nbp` | artefatto da generare Formato Wolfram Player/proprietario: richiede un export/conversione reale del frontend compatibile. Non viene rinominato il codice .wl come documento serializzato. |
| `.wl` | [hello.wl](hello.wl) verificato |
| `.wls` | [hello.wls](variants/wls-852bcca4/hello.wls) creato, verifiche pendenti |
| `.wlt` | [hello.wlt](variants/wlt-5420c4e1/hello.wlt) creato, verifiche pendenti |
