# #351 KDL

Voce canonica `KDL`, tipo `data`, language_id `931123626`.

Rappresentare il saluto come valore di un nodo nel KDL Document Language e verificarne dati e proprietà.

## Toolchain e riproduzione

Existing KDL-JS document parser — kdljs 0.3.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

KDL-JS 0.3.0 su Node.js 22.20.0. Il documento usa una forma compatibile del node language: greeting, valore stringa e proprietà language=en.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools kdljs@0.3.0; node verify.cjs .tools
```

Risultato atteso: Un solo nodo greeting, valore Hello, World!, language=en; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

L’implementazione esistente analizza il documento e deve riportare zero errori. I flag riguardano il modello dati letto dal parser; non una applicazione che consumi quel modello.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://kdl.dev/spec/](https://kdl.dev/spec/)
- [https://github.com/kdl-org/kdl-js](https://github.com/kdl-org/kdl-js)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kdl` | [hello.kdl](hello.kdl) verificato |
