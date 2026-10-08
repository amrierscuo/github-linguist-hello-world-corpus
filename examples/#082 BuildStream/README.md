# #082 BuildStream

Importare hello.txt in un artefatto BuildStream e leggere Hello, World! dall'artefatto esportato.

## Toolchain

BuildStream 2.x, progetto con min-version 2.0; toolchain non eseguita e versione concreta da registrare.

## Comandi e procedura

Dalla cartella dell'esempio, che contiene project.conf:

```sh
bst --version
bst show hello.bst
bst build hello.bst
bst artifact checkout --directory build-artifact hello.bst
cat build-artifact/hello.txt
```

BuildStream gestisce propria cache di sorgenti e artefatti. L'elemento importa
il file hello.txt dal progetto; il checkout rende verificabile il risultato.
Registrare toolchain e log della build prima di accreditare la verifica.

## Risultato atteso

Build dell'elemento import e checkout senza errori; hello.txt nell'artefatto contiene esattamente Hello, World! più newline.

## Stato

Sintassi e semantica in attesa.

project.conf fornisce il contesto del progetto; elements/hello.bst usa la sorgente local e il plugin import. Un parser YAML non prova un build BuildStream.

Requisiti residui:
- BuildStream e backend cache/sandbox non disponibili: parsing del progetto e build/check-out non eseguiti.

## Fonti primarie

- [https://docs.buildstream.build/master/tutorial/first-project.html](https://docs.buildstream.build/master/tutorial/first-project.html)
- [https://docs.buildstream.build/2.3/format_project.html](https://docs.buildstream.build/2.3/format_project.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bst` | [hello.bst](elements/hello.bst) creato, verifiche pendenti |
