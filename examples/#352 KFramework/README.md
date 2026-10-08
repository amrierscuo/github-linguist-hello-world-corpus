# #352 KFramework

Voce canonica `KFramework`, tipo `programming`, language_id `9479532`.

Definire una piccola semantica K che riscrive il termine hello nel valore stringa del saluto nella cella k.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede K Framework con backend configurato e i moduli builtin STRING. I prodotti del compilatore devono restare in una copia di lavoro.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
kompile hello.k --main-module HELLO --syntax-module HELLO; krun input.hello
```

Risultato atteso: Definizione compilata; cella k finale contiene "Hello, World!".

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

La regola è una vera riscrittura semantica K; manca la toolchain kompile/krun. Non vengono interpretate le regole con un simulatore fatto in casa.

Requisiti residui:

- K Framework kompile/krun and backend are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://kframework.org/docs/user_manual/](https://kframework.org/docs/user_manual/)
- [https://github.com/runtimeverification/k](https://github.com/runtimeverification/k)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.k` | [hello.k](hello.k) creato, verifiche pendenti |
