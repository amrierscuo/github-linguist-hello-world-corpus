# #248 Git Config

Leggere con Git una configurazione corpus.greeting che contiene Hello, World!.

## Toolchain

git version 2.51.0.windows.1

## Comandi e procedura

python verify.py 248 /percorso/nuovo-repo-temporaneo git

## Risultato atteso

git config --file .gitconfig --get corpus.greeting restituisce il saluto più newline.

## Stato

Sintassi e semantica verificate.

La sezione corpus è metadata illustrativo letto dal parser Git originale. Il flag --file seleziona il file incluso; nessuna configurazione globale viene cambiata.

Verifica effettiva del 2026-10-08T12:15:30.771284+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gitconfig` | [.gitconfig](.gitconfig) verificato |
