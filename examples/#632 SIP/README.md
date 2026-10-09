# #632 SIP

Voce e ordine canonici di `reference/languages.yml`. Sorgente e fixture originali.

## Obiettivo

Generare e compilare binding Python per una funzione C che restituisce `Hello, World!`, poi importare l'estensione e chiamare la funzione.

`hello.sip` contiene la descrizione SIP e il corpo C. Il codice generato, i file oggetto e l'estensione compilata restano nella directory temporanea della prova.

## Toolchain e riproduzione

Prova autentica con SIP 6.17.0, CPython 3.12.3, setuptools 84.0.0 e GCC 13.3.0 su Ubuntu 24.04 WSL2 x86_64.

Copiare `hello.sip`, `pyproject.toml` e `verify_runtime.py` in una directory temporanea. Servono un compilatore C e gli header di sviluppo di Python. Dalla copia dell'esempio, con SIP installato nel Python scelto:

```sh
python -m sipbuild.tools.build --build-dir build --verbose
PYTHONPATH=build/corpus_greeting/build/lib.linux-x86_64-cpython-312 python verify_runtime.py
```

Il percorso di `PYTHONPATH` qui riportato è quello prodotto nella prova CPython 3.12 su Linux x86_64. Per un altro interprete o sistema usare la directory che contiene il modulo `corpus_greeting` compilato, senza copiare il binario nel corpus.

## Risultato atteso e stato

`verify_runtime.py` importa l'estensione compilata, chiama `corpus_greeting.corpus_greeting()`, verifica il valore restituito e stampa:

```text
Hello, World!
```

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

La generazione dei wrapper, la compilazione, il linking e l'import con chiamata C terminano con exit code 0. La precedente prova di sola generazione è conservata in [verification/toolchain.json](verification/toolchain.json). La nuova prova completa è [verification/runtime.json](verification/runtime.json), con versioni, comandi, ambiente rilevante, output e SHA-256 dei sorgenti e del binario effettivamente importato. I percorsi personali sono sostituiti con placeholder.

## Fonti primarie

- [Direttiva Module](https://python-sip.readthedocs.io/en/latest/directives.html#directive-Module)
- [Strumenti di compilazione SIP](https://python-sip.readthedocs.io/en/stable/command_line_tools.html)
- [Distribuzione SIP 6.17.0](https://pypi.org/project/sip/6.17.0/)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.sip` | [hello.sip](hello.sip) sintassi e semantica verificate |
