# #247 Git Commit

Usare un messaggio di commit Git originale con subject Hello, World! e verificarlo nel commit creato.

## Toolchain

git version 2.51.0.windows.1

## Comandi e procedura

python verify.py 247 /percorso/nuovo-repo-temporaneo git

## Risultato atteso

Commit locale creato; git log restituisce il subject Hello, World!; cat-file preserva il corpo di .gitmessage.

## Stato

Sintassi e semantica verificate.

verify.py usa commit -F e --cleanup=verbatim nel repository temporaneo. Identità e date sono fixture illustrative deterministiche, senza dati personali. Nessun commit viene creato nel corpus.

Verifica effettiva del 2026-10-08T12:15:30.149179+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://git-scm.com/docs/git-commit](https://git-scm.com/docs/git-commit)
- [https://git-scm.com/docs/git-log](https://git-scm.com/docs/git-log)
- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
