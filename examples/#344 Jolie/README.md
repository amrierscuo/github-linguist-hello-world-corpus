# #344 Jolie

Voce canonica `Jolie`, tipo `programming`, language_id `998078858`.

Invocare la libreria Console Jolie per stampare il saluto dal blocco main.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede l’interprete Jolie e console.iol della stessa distribuzione, con JVM compatibile. Il programma invoca println@Console secondo il protocollo della libreria.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
jolie hello.ol
```

Risultato atteso: Jolie accetta ed esegue il programma; Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

L’interprete e la libreria non sono configurati; non si deduce validità dalla somiglianza con altri linguaggi.

Requisiti residui:

- Jolie interpreter and console.iol standard library are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.jolie-lang.org/](https://www.jolie-lang.org/)
- [https://docs.jolie-lang.org/v1.12.x/language-tools-and-standard-library/basics/fault-handling/scopes-and-faults/README.html](https://docs.jolie-lang.org/v1.12.x/language-tools-and-standard-library/basics/fault-handling/scopes-and-faults/README.html)
- [https://github.com/jolie/jolie](https://github.com/jolie/jolie)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ol` | [hello.ol](hello.ol) creato, verifiche pendenti |
| `.iol` | [hello.iol](variants/iol-77ad5fa4/hello.iol) creato, verifiche pendenti |
