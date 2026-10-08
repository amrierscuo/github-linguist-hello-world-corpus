# #312 Inform 7

Compilare una storia Inform 7 che saluta all’avvio e termina.

## Toolchain

inform7 version 10.1.2 'Krypton' (29 August 2022); Inform 6 Inform 6.41 for Linux (22nd July 2022); Frotz 2.54

## Comandi e procedura

inform7 -internal <risorse-vendor> -external build/external -transient build/transient -no-index -no-problems -no-census-update -format=Inform6/16 -source hello.ni -o build/hello.inf; inform6 -wSDv8 build/hello.inf build/hello.z8; dfrotz -m build/hello.z8 (stdin: quit più newline)

## Risultato atteso

Transcript contiene Hello, World!; quit chiude il menu finale e il runtime termina con exit 0.

## Stato

Sintassi e semantica verificate.

Le regole in linguaggio naturale sono compilate da Inform 7, tradotte nel backend Inform 6 e interpretate da Frotz come vera storia Z-machine v8. Il menu finale standard fa parte del transcript; non si richiede stdout composto soltanto dal saluto. Story/Inter/output binari restano in work.

Verifica effettiva del 2026-10-08T12:34:30.772531+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://github.com/ganelson/inform/releases/tag/v10.1.2](https://github.com/ganelson/inform/releases/tag/v10.1.2)
- [https://ganelson.github.io/inform-website/](https://ganelson.github.io/inform-website/)
- [https://davidgriffith.gitlab.io/frotz/](https://davidgriffith.gitlab.io/frotz/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ni` | [hello.ni](hello.ni), [hello.ni](variants/i7x-25250f70/hello.ni) creato, verifiche pendenti |
| `.i7x` | [Corpus Greeting.i7x](variants/i7x-25250f70/Corpus%20Greeting.i7x) creato, verifiche pendenti |
