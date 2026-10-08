# #460 NSIS

Voce canonica `NSIS`, tipo `programming`, language_id `242`.

Compilare un installer NSIS originale il cui Section mostra il saluto e termina.

## Toolchain e riproduzione

Official NSIS script compiler and native Windows installer generator — v3.09-4. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

NSIS 3.09-4 autentico con Stubs della distribuzione; eseguire il compiler con cwd build per lasciare l’EXE fuori dal corpus.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
makensis -NOCD hello.nsi
```

Risultato atteso: Compilazione exit 0, installer prodotto; futura UI mostrerebbe Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Compiler autentico produce un installer Windows, SHA nel log. Per l’ambito concordato non viene eseguito né installato; semantica pending.

Requisiti residui:

- Installer script compiled; installer execution is intentionally not performed in this verification scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://nsis.sourceforge.io/Docs/Chapter4.html](https://nsis.sourceforge.io/Docs/Chapter4.html)
- [https://nsis.sourceforge.io/Docs/](https://nsis.sourceforge.io/Docs/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nsi` | [hello.nsi](hello.nsi), [driver.nsi](variants/nsh-90f0ff9b/driver.nsi) creato, verifiche pendenti |
| `.nsh` | [hello.nsh](variants/nsh-90f0ff9b/hello.nsh) creato, verifiche pendenti |
