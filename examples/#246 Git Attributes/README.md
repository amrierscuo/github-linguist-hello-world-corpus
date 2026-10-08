# #246 Git Attributes

Applicare attributi Git al file Hello, World!: testo con newline LF e metadata corpus-greeting=hello-world.

## Toolchain

git version 2.51.0.windows.1

## Comandi e procedura

python verify.py 246 /percorso/nuovo-repo-temporaneo git

## Risultato atteso

check-attr restituisce text=set, eol=lf, corpus-greeting=hello-world; Git index contiene Hello, World! con LF.

## Stato

Sintassi e semantica verificate.

Il saluto è nel file hello.txt. L’attributo custom ha un valore senza spazi valido per il formato .gitattributes. La fixture crea un repository separato e disabilita lettura/modifica della configurazione globale.

Verifica effettiva del 2026-10-08T12:15:29.811553+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://git-scm.com/docs/gitattributes](https://git-scm.com/docs/gitattributes)
- [https://git-scm.com/docs/git-check-attr](https://git-scm.com/docs/git-check-attr)
