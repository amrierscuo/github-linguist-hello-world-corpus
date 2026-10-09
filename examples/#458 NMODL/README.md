# #458 NMODL

Voce canonica `NMODL`, tipo `programming`, `language_id: 136456478`.

## Obiettivo

Compilare e caricare un meccanismo NMODL che stampa il saluto durante `INITIAL`, eseguito da `finitialize` in NEURON.

## Toolchain e riproduzione

Prova autentica con NEURON 9.0.1, CPython 3.12.3 e GCC 13.3.0 su Ubuntu 24.04 WSL2 x86_64. Il runtime deriva dal wheel Linux ufficiale NEURON; compilatore e header di sviluppo devono essere disponibili.

Copiare `greeting.mod` e `check.hoc` in una directory temporanea. Dopo aver installato NEURON nel Python scelto e reso disponibili `nrnivmodl` e `nrniv` nel PATH:

```sh
nrnivmodl greeting.mod
nrniv -nogui check.hoc
```

`nrnivmodl` traduce il sorgente in C++, compila il meccanismo e crea `x86_64/libnrnmech.so`. `nrniv` carica la libreria dalla directory corrente. `check.hoc` crea una sezione `soma`, esegue `insert greeting` e chiama `finitialize(-65)`.

## Risultato atteso e stato

L'esecuzione di `INITIAL` stampa una riga `Hello, World!`. La console HOC mostra anche il valore di ritorno `1` di `finitialize`; il banner e l'elenco dei meccanismi caricati sono su stderr.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

La traduzione, la compilazione e il linking terminano con exit code 0. Il processo NEURON carica `greeting.mod`, lo inserisce nella sezione e produce il saluto una sola volta durante l'inizializzazione. La prova precedente con `nocmodl` 8.2.2 resta in [verification/native.json](verification/native.json). La nuova prova completa è [verification/runtime.json](verification/runtime.json), con versioni, comandi, output, ambiente rilevante e SHA-256 dei sorgenti e della libreria compilata. Le sorgenti originali non sono cambiate.

Il log di compilazione conserva un avviso `make` sullo scarto di clock del filesystem montato, pari a 0,013 secondi. Linking, caricamento ed esecuzione del meccanismo sono riusciti. I prodotti compilati e le dipendenze restano fuori dal corpus.

## Fonti primarie

- [Linguaggio NMODL e INITIAL](https://www.neuronsimulator.org/en/latest/nmodl/language/nmodl.html#initial)
- [Installazione ufficiale e compilazione dei file MOD](https://www.neuronsimulator.org/en/latest/install/install_instructions.html)
- [Distribuzione NEURON 9.0.1](https://pypi.org/project/neuron/9.0.1/)
- [Documentazione originaria dell'esempio](https://www.neuronsimulator.org/en/latest/nmodl/NMODL_language.html)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.mod` | [greeting.mod](greeting.mod) sintassi e semantica verificate |
