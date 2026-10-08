# #347 Julia REPL

Voce canonica `Julia REPL`, tipo `programming`, language_id `220689142`.

Registrare una vera sessione Julia REPL con prompt, valore di assegnamento, stampa del saluto e uscita.

## Toolchain e riproduzione

Official Julia native runtime and actual terminal REPL — julia version 1.13.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Julia ufficiale 1.13.1 e pywinpty già presente su Windows. Il helper usa un terminale ConPTY senza finestra visibile, TERM=dumb e depot isolata. repl-input.txt contiene i comandi originali; replay.jl è una forma batch ausiliaria dello stesso saluto.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify_repl.py <julia.exe> build; oppure julia --startup-file=no --history-file=no --color=no --banner=no e digitare le righe di repl-input.txt
```

Risultato atteso: Prompt julia>, valore "World", Hello, World!, prompt exit(); PASS della vera sessione.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

hello.julia-repl.txt è il transcript catturato realmente, distinto dal normale sorgente Julia. Il log conserva l’output terminale grezzo; il transcript rimuove solo controlli VT/cursore, normalizza CRLF e righe vuote, e omette l’avviso di terminale prima del primo prompt. Il controllo richiede prompt, valore "World", stampa e exit 0.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.julialang.org/en/v1/stdlib/REPL/](https://docs.julialang.org/en/v1/stdlib/REPL/)
- [https://docs.julialang.org/en/v1/manual/command-line-interface/](https://docs.julialang.org/en/v1/manual/command-line-interface/)
- [https://github.com/andfoy/pywinpty](https://github.com/andfoy/pywinpty)
