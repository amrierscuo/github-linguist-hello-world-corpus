# #388 Linux Kernel Module

Associare metadata .mod e Kbuild al modulo originale che contiene il saluto.

## Toolchain

Linux kernel headers/toolchain Kbuild compatibili; versione da registrare

## Comandi e procedura

Copiare Kbuild/hello.c in build; make -C <kernel-headers> M=<percorso-assoluto-build> modules; confrontare hello.mod normalizzando il prefisso della cartella oggetti

## Risultato atteso

Kbuild genera hello.mod riferito a hello.o; build offline accettata; modulo contiene il messaggio e MODULE_DESCRIPTION del saluto.

## Stato

Sintassi e semantica in attesa.

Linux Kernel Module nella baseline è un formato dati .mod. hello.mod è il campione testuale della lista oggetti, con percorso relativo illustrativo; Kbuild e hello.c ne forniscono il contesto reale. Non è un binario .ko e non può essere caricato direttamente. La futura verifica prevista è compilazione/metadata offline; init/runtime kernel non è attestato.

Requisiti residui:
- Header/build tree kernel Kbuild non preparati; compilazione offline e rigenerazione .mod pending.

## Fonti primarie

- [https://docs.kernel.org/kbuild/modules.html](https://docs.kernel.org/kbuild/modules.html)
- [https://docs.kernel.org/kbuild/makefiles.html](https://docs.kernel.org/kbuild/makefiles.html)
- [https://github.com/torvalds/linux/blob/master/scripts/Makefile.build](https://github.com/torvalds/linux/blob/master/scripts/Makefile.build)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mod` | [hello.mod](hello.mod) creato, verifiche pendenti |
