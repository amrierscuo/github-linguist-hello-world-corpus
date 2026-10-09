# #353 KRL

Voce canonica `KRL`, tipo `programming`, language_id `186`.

Il ruleset reagisce all'evento `corpus:hello` e invia una direttiva `greeting` con `message=Hello, World!`.

## Toolchain e riproduzione

Picolab Pico Engine core 1.6.4, pico-framework 0.8.1, krl-compiler e krl-parser 1.5.0, Node.js 22.20.0. La baseline Linguist identifica qui Kinetic Rule Language.

Dalla directory dell'esempio, con dipendenze in una cartella dedicata esterna ai sorgenti del corpus:

```sh
npm install --prefix /path/to/krl-tools pico-engine-core@1.6.4 memory-level@1.0.0 charwise@3.0.1
node verify.cjs /path/to/krl-tools /path/to/krl-build
node verify_runtime.cjs /path/to/krl-tools
```

Sostituire `/path/to` con cartelle di lavoro proprie, esterne al clone. Il checker carica i byte di `hello.krl` attraverso il loader ufficiale, li compila con il compilatore originale e installa il ruleset in un pico reale del motore. Il database e il loader sono in memoria. Non si avvia un server HTTP e non viene scaricato codice remoto per il ruleset.

## Stato ed evidenza

Artefatto creato, sintassi verificata, semantica verificata su Windows x64.

Il test invia prima `corpus:unrelated`, che non genera direttive, e poi `corpus:hello`. Il risultato effettivo contiene una sola direttiva `greeting` con `options.message` uguale a `Hello, World!`. Il ruleset viene disinstallato e il database chiuso al termine.

Log reale: [runtime.json](verification/runtime.json), con timestamp UTC, versioni, comandi, exit code, output, hash dei sorgenti e del checker. La precedente prova di solo parsing resta in [native.json](verification/native.json). Le dipendenze e l'AST generato rimangono esterni al corpus.

## Fonti primarie

- [Picolab Pico Engine e componenti ufficiali](https://github.com/Picolab/pico-engine)
- [Picolab pico-framework](https://github.com/Picolab/pico-framework)
- [Grammatica KRL](https://picolabs.atlassian.net/wiki/spaces/docs/pages/223117313/Grammar)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.krl` | [hello.krl](hello.krl) sintassi e semantica verificate |
