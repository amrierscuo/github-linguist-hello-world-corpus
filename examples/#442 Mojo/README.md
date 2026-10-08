# #442 Mojo

Voce canonica `Mojo`, tipo `programming`, language_id `1045019587`.

Stampare il saluto dal punto di ingresso fn main di Mojo.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede la distribuzione ufficiale Modular Mojo con runtime compatibile.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
mojo hello.mojo
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente originale; compiler/runtime non configurati.

Requisiti residui:

- Mojo compiler/runtime is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.modular.com/mojo/manual/basics](https://docs.modular.com/mojo/manual/basics)
- [https://docs.modular.com/mojo/quickstart](https://docs.modular.com/mojo/quickstart)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mojo` | [hello.mojo](hello.mojo) creato, verifiche pendenti |
