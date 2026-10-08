# #249 Git Revision List

Ignorare con git blame una revisione cosmetica reale che aggiunge lo spazio in Hello, World!.

## Toolchain

git version 2.51.0.windows.1

## Comandi e procedura

python verify.py 249 /percorso/nuovo-repo-temporaneo git

## Risultato atteso

Senza ignore: riga attribuita al commit di formattazione; con la lista: attribuita al commit precedente; testo finale Hello, World!.

## Stato

Sintassi e semantica verificate.

La lista contiene il vero object ID del secondo commit della fixture riproducibile; non un hash inventato. verify.py ricrea i commit con identità/date deterministiche e confronta il valore registrato. Gli ID riguardano questo repository temporaneo e non la storia futura del corpus pubblico.

Verifica effettiva del 2026-10-08T12:15:32.429631+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---ignore-revs-fileltfilegt](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---ignore-revs-fileltfilegt)
