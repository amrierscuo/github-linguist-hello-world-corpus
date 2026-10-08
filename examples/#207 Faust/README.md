# #207 Faust

Voce canonica `Faust`, tipo `programming`, language_id `622529198`.

Generare un DSP Faust con tredici canali costanti ASCII e ricostruire il saluto da un frame audio realmente calcolato.

## Toolchain e riproduzione

Official Faust compiler extracted from Ubuntu package — Faust 2.70.3; GCC 13.3.0. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Faust 2.70.3 e GNU G++ 13.3.0 su Ubuntu. Per la distribuzione estratta localmente usare LD_LIBRARY_PATH delle librerie Faust. Il file generato e il binario restano nella directory build.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
faust -lang cpp -cn GreetingDSP -o build/GreetingDSP.h hello.dsp; g++ -std=c++17 -O2 -I build verify.cpp -o build/check; ./build/check
```

Risultato atteso: Hello, World! e PASS delle asserzioni sui campioni.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

verify.cpp fornisce le interfacce dell’architettura DSP e invoca init/compute del codice autenticamente generato. Controlla zero ingressi, tredici uscite e tredici campioni ASCII; non riscrive la logica DSP in C++.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://faustdoc.grame.fr/manual/syntax/](https://faustdoc.grame.fr/manual/syntax/)
- [https://faustdoc.grame.fr/manual/compiler/](https://faustdoc.grame.fr/manual/compiler/)
- [https://faustdoc.grame.fr/manual/architectures/](https://faustdoc.grame.fr/manual/architectures/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dsp` | [hello.dsp](hello.dsp) verificato |
