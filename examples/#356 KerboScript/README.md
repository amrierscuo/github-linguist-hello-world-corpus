# #356 KerboScript

Voce canonica `KerboScript`, tipo `programming`, language_id `59716426`.

Eseguire un programma KerboScript che concatena una variabile e stampa il saluto sulla console kOS.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Kerbal Space Program con il mod kOS e una CPU di bordo. Copiare il file nel volume disponibile. Il programma non pilota un veicolo o modifica controlli di volo.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Nel terminale kOS di KSP: RUNPATH("hello.ks").
```

Risultato atteso: Console kOS emette Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

SET/TO e PRINT con terminatori . sono sorgente KerboScript. Il gioco/runtime non è disponibile, quindi i flag restano pendenti.

Requisiti residui:

- Kerbal Space Program with the kOS mod/runtime is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://ksp-kos.github.io/KOS/language/variables.html](https://ksp-kos.github.io/KOS/language/variables.html)
- [https://ksp-kos.github.io/KOS/language/flow.html](https://ksp-kos.github.io/KOS/language/flow.html)
- [https://github.com/KSP-KOS/KOS](https://github.com/KSP-KOS/KOS)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ks` | [hello.ks](hello.ks) creato, verifiche pendenti |
