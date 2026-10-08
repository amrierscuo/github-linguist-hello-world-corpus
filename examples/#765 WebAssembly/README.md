# #765 WebAssembly

Voce canonica `WebAssembly`, tipo `programming`, language_id `956556503`.

Modulo WebAssembly in formato testuale WAT, con memoria contenente il saluto e funzioni esportate che ne restituiscono posizione e lunghezza.

## Toolchain e riproduzione

wabt / Node.js 22.20.0 — 1.0.39. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Node.js 22.20.0 e pacchetto npm wabt, versione nel log. `<prefisso-npm>/node_modules/wabt` deve esistere; il secondo argomento è una directory esterna già creata, dove scrivere hello.wasm.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
node verify.cjs <prefisso-npm> <directory-output-esterna>
```

Risultato atteso: Hello, World! e PASS dopo compilazione, istanziazione e lettura della memoria.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

WABT esegue parseWat, resolveNames, validate e compilazione. Il motore WebAssembly nativo di Node istanzia il bytecode; il driver invoca gli export e legge realmente la memoria per ottenere il saluto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://webassembly.github.io/spec/core/text/modules.html](https://webassembly.github.io/spec/core/text/modules.html)
- [https://github.com/WebAssembly/wabt](https://github.com/WebAssembly/wabt)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.wast` | [hello.wast](variants/wast-39778c33/hello.wast) creato, verifiche pendenti |
| `.wat` | [hello.wat](hello.wat) verificato |
