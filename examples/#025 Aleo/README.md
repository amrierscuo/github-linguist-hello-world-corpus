# #025 Aleo

Voce canonica: `Aleo`, tipo `programming`, `language_id: 566431048`.
`hello.aleo` è scritto in Aleo Instructions. La funzione `greeting`, senza
argomenti, costruisce un array pubblico di tredici `u8` che codifica
`Hello, World!` in ASCII. È una funzione locale del programma
`corpus_hello_world.aleo`; non è un deployment.

## Toolchain e riproduzione

Parser verificato su Windows x64 con Node.js **22.20.0** e pacchetto ufficiale
**@provablehq/wasm 0.12.0, mainnet**; SDK 0.12.0 disponibile nell'ambiente.
Il verificatore importa direttamente i binding WASM SnarkVM. Dalla directory
di questo esempio:

```powershell
npm --prefix .tools install --no-audit --no-fund --save-exact @provablehq/wasm@0.12.0
node verify.cjs .tools/node_modules hello.aleo --syntax-only
```

Risultato della prova sintattica: `Program.fromString` accetta il programma,
espone soltanto `greeting` senza input e rifiuta un'istruzione inesistente.
Entrambe le asserzioni producono `PASS` e il processo termina con codice 0.
Per la prova semantica ancora da completare:

```powershell
node verify.cjs .tools/node_modules hello.aleo
```

Quest'ultimo comando usa una chiave effimera non stampata ed esegue la funzione
offline con `prove_execution=false`; può richiedere l'inizializzazione dei parametri
SnarkVM. L'output atteso è
`[72u8, 101u8, 108u8, 108u8, 111u8, 44u8, 32u8, 87u8, 111u8, 114u8, 108u8, 100u8, 33u8]`.

## Stato ed evidenza

Artefatto creato; sintassi **verificata**; semantica **in attesa**.
Requisito residuo: ottenere un'esecuzione VM offline completa con i parametri
necessari e conservarne il risultato. Il precedente tentativo via SDK non ha
fornito un log completo di esecuzione e non viene conteggiato. La prova corrente
è limitata a parsing e firma della funzione; i temporanei XHR di quel tentativo
sono stati spostati fuori dal corpus.

Log: [aleo-wasm.json](verification/aleo-wasm.json), con output del parser,
versione, SHA-256 del sorgente e del verificatore. `path_normalization` descrive
i percorsi normalizzati; nessun risultato di esecuzione VM è attestato.

## Fonti ufficiali

- [Tipi e costruzione di array Aleo](https://docs.aleo.org/build/aleo-instructions/reference/types/index.html).
- [SDK e binding SnarkVM WASM ufficiali](https://github.com/ProvableHQ/sdk).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.aleo` | [hello.aleo](hello.aleo) sintassi verificata |
