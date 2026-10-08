# #265 Grace

Voce canonica `Grace`, tipo `programming`, language_id `135`.

Interpolare una binding immutabile in Grace e stampare il risultato con il dialetto standard.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Minigrace e i moduli del dialetto standard. Il compiler self-hosted genera JavaScript; compilare in una copia di lavoro per conservare il sorgente pulito.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
minigrace-js hello.grace
```

Risultato atteso: Compilazione ed esecuzione del sorgente producono Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

La sintassi di print senza parentesi e interpolazione {name} segue Grace. Non sono configurati il compiler e i moduli, quindi i flag restano false.

Requisiti residui:

- Minigrace compiler and standard dialect modules are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/gracelang/minigrace](https://github.com/gracelang/minigrace)
- [https://github.com/gracelang/language](https://github.com/gracelang/language)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.grace` | [hello.grace](hello.grace) creato, verifiche pendenti |
