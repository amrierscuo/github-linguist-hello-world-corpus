# #458 NMODL

Voce canonica `NMODL`, tipo `programming`, language_id `136456478`.

Tradurre un meccanismo NMODL che stampa il saluto durante INITIAL.

## Toolchain e riproduzione

Original NEURON NMODL-to-C compiler — NEURON Ubuntu package 8.2.2-6build2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler nocmodl autentico da NEURON 8.2.2-6build2; esecuzione richiede librerie e linking del runtime NEURON.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
nrnivmodl greeting.mod; nrniv -nogui check.hoc
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

nocmodl traduce il sorgente in C senza errore. Caricamento, insert e finitialize non sono eseguiti; semantica pending.

Requisiti residui:

- NMODL parser/code generator accepted the mechanism; linking/loading the mechanism and finitialize in NEURON are not performed.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.neuronsimulator.org/en/latest/nmodl/NMODL_language.html](https://www.neuronsimulator.org/en/latest/nmodl/NMODL_language.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mod` | [greeting.mod](greeting.mod) sintassi verificata |
