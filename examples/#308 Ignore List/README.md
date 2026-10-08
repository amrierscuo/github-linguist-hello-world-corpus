# #308 Ignore List

Applicare una Ignore List Git, escludendo build e file generati ma conservando il file del saluto.

## Toolchain

git version 2.51.0.windows.1

## Comandi e procedura

python verify.py /percorso/nuovo-repo-temporaneo git

## Risultato atteso

build/disposable.txt e other.generated.txt ignorati; hello.generated.txt conservato e contiene Hello, World!.

## Stato

Sintassi e semantica verificate.

La fixture crea un vero repository separato, legge .gitignore e prova anche l’eccezione con !. Nessuna configurazione globale o repository del corpus viene modificato.

Verifica effettiva del 2026-10-08T12:29:57.452856+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://git-scm.com/docs/gitignore](https://git-scm.com/docs/gitignore)
- [https://git-scm.com/docs/git-check-ignore](https://git-scm.com/docs/git-check-ignore)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gitignore` | [.gitignore](.gitignore) verificato |
