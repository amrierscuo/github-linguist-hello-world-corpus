# #241 Gentoo Ebuild

Installare uno script originale hello-world attraverso la fase src_install di un ebuild EAPI 8.

## Toolchain

GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)

## Comandi e procedura

bash -n hello-world-1.0.ebuild; ebuild hello-world-1.0.ebuild install; eseguire hello-world dall’immagine di installazione temporanea

## Risultato atteso

Sintassi Bash accettata; Portage installa binario shell che stampa Hello, World! più newline.

## Stato

Sintassi verificata; semantica in attesa.

La verifica presente è limitata al parser Bash reale e alla fixture shell originale, che stampa il saluto. Le funzioni newbin e le fasi EAPI non sono simulate: l’installazione Portage resta pending. L’URL example.invalid è illustrativo e il pacchetto non scarica sorgenti.

Verifica effettiva del 2026-10-08T12:15:42.652678+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

Requisiti residui:
- Gentoo Portage package environment not available: native install/inherit phases pending.

## Fonti primarie

- [https://devmanual.gentoo.org/ebuild-writing/file-format/index.html](https://devmanual.gentoo.org/ebuild-writing/file-format/index.html)
- [https://devmanual.gentoo.org/ebuild-writing/functions/src_install/index.html](https://devmanual.gentoo.org/ebuild-writing/functions/src_install/index.html)
- [https://projects.gentoo.org/pms/latest/pms.html](https://projects.gentoo.org/pms/latest/pms.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ebuild` | [hello-world-1.0.ebuild](hello-world-1.0.ebuild) sintassi verificata |
