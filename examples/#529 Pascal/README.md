# #529 Pascal

Voce canonica `Pascal`, tipo `programming`, language_id `281`.

Compilare ed eseguire un programma Pascal con WriteLn.

## Toolchain e riproduzione

Genuine Free Pascal compiler — 3.2.2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Free Pascal 3.2.2 ufficiale; compiler e units RTL estratti sotto work. Il log contiene i percorsi reali del compiler relocato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
fpc -FEbuild -FUbuild hello.pas; build/hello
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Compiler genuino genera un programma nativo che stampa esattamente il saluto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.freepascal.org/docs.html](https://www.freepascal.org/docs.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pas` | [hello.pas](hello.pas), [driver.pas](variants/inc-dd126fb7/driver.pas) creato, verifiche pendenti |
| `.dfm` | [hello.dfm](variants/dfm-e05beb09/hello.dfm) creato, verifiche pendenti |
| `.dpr` | [hello.dpr](variants/dpr-30850e89/hello.dpr) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
| `.lpr` | [hello.lpr](variants/lpr-3e546050/hello.lpr) creato, verifiche pendenti |
| `.pascal` | [hello.pascal](variants/pascal-539d0d7d/hello.pascal) creato, verifiche pendenti |
| `.pp` | [hello.pp](variants/pp-60aacc63/hello.pp) creato, verifiche pendenti |
