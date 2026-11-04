# #458 NMODL

Voce canonica `NMODL`, tipo `programming`, `language_id: 136456478`.

## Goal

Fill and load a NMODL mechanism that prints greetings during `INITIAL`, executed by `finitialize` in NEURON.

## Toolchain and reproduction

Authentic test with NEURON 9.0.1, CPython 3.12.3 and GCC 13.3.0 on Ubuntu 24.04 WSL2 x86_64. The runtime comes from the official Linux wheel NEURON; compiler and development header must be available.

Copy `greeting.mod` and `check.hoc` in a temporary directory. After installing NEURON in the chosen Python and made available `nrnivmodl` and `nrniv` in PATH:

```sh
nrnivmodl greeting.mod
nrniv -nogui check.hoc
```

`nrnivmodl` translates the source into C++, compiles the mechanism and creates `x86_64/libnrnmech.so`. `nrniv` loads the library from the current directory. `check.hoc` creates a `soma` section, performs `insert greeting` and calls `finitialize(-65)`.

## Expected result and status

L'esecuzione di `INITIAL` stampa una riga `Hello, World!`. La console HOC mostra anche il valore di ritorno `1` di `finitialize`; il banner e l'elenco dei meccanismi caricati sono su stderr.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

La traduzione, la compilazione e il linking terminano con exit code 0. Il processo NEURON carica `greeting.mod`, lo inserisce nella sezione e produce il saluto una sola volta durante l'inizializzazione. La prova precedente con `nocmodl` 8.2.2 resta in [verification/native.json](verification/native.json). La nuova prova completa è [verification/runtime.json](verification/runtime.json), con versioni, comandi, output, ambiente rilevante e SHA-256 dei sorgenti e della libreria compilata. Le sorgenti originali non sono cambiate.

The compilation log keeps a `make` warning on the clock scrap of the mounted filesystem, equal to 0, 013 seconds. Linking, loading and running the mechanism have been successful.

## Primary sources

- [Linguaggio NMODL e INITIAL](https://www.neuronsimulator.org/en/latest/nmodl/language/nmodl.html#initial)
- [Installazione ufficiale e compilazione dei file MOD](https://www.neuronsimulator.org/en/latest/install/install_instructions.html)
- [Distribuzione NEURON 9.0.1](https://pypi.org/project/neuron/9.0.1/)
- [Documentazione originaria dell'esempio](https://www.neuronsimulator.org/en/latest/nmodl/NMODL_language.html)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.mod` | [greeting.mod](greeting.mod) syntax and behavior verified |
