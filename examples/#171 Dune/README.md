# #171 Dune

Leggere un progetto Dune e costruire l’alias hello che esegue echo del saluto.

## Toolchain

Dune 3.14.0; OCaml 4.14.1

## Comandi e procedura

dune --version; ocamlc -version; dune build --display quiet @hello

## Risultato atteso

Build exit 0; action echo scrive Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

dune-project è il nome canonico riconosciuto dalla voce Linguist; dune contiene la regola di supporto. Anche una regola solo echo richiede a Dune un contesto OCaml reale. Build e dipendenze locali rimangono sotto work durante la verifica.

Verifica effettiva del 2026-10-08T12:01:45.272622+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://dune.readthedocs.io/en/stable/reference/dune-project/index.html](https://dune.readthedocs.io/en/stable/reference/dune-project/index.html)
- [https://dune.readthedocs.io/en/stable/reference/dune/rule.html](https://dune.readthedocs.io/en/stable/reference/dune/rule.html)
- [https://dune.readthedocs.io/en/stable/reference/actions/echo.html](https://dune.readthedocs.io/en/stable/reference/actions/echo.html)
