# #166 Diff

Applicare una patch unified diff che trasforma Hello in Hello, World!.

## Toolchain

GNU GNU patch 2.7.6; diff (GNU diffutils) 3.10

## Comandi e procedura

diff -u --label a/hello.txt before/hello.txt --label b/hello.txt after/hello.txt; copiare before/hello.txt in build/hello.txt; da build: patch --batch -p1 -i ../hello.diff

## Risultato atteso

diff exit 1 perché esistono differenze; patch exit 0; file risultante uguale a after/hello.txt.

## Stato

Sintassi e semantica verificate.

La patch inclusa è confrontata byte per byte con GNU diff. patch la applica in una directory temporanea; il saluto nel file risultante è verificato. Exit 1 da diff è il codice corretto per file differenti.

Verifica effettiva del 2026-10-08T11:56:12.780978+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html](https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html)
- [https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html](https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.diff` | [hello.diff](hello.diff) verificato |
| `.patch` | [hello.patch](variants/ext-patch-2e7061746368/hello.patch) creato, verifiche pendenti |
