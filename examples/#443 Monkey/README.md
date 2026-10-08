# #443 Monkey

Voce canonica `Monkey`, tipo `programming`, language_id `236`.

Eseguire Main con Print nel linguaggio Monkey X originale.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Monkey X transcc e backend StdCpp/C++ della stessa distribuzione.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
transcc -target=StdCpp -run hello.monkey
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Monkey X e Monkey C sono voci distinte; il programma usa Strict, Main:Int e Print. Toolchain assente.

Requisiti residui:

- Monkey X transcc compiler/backend is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/blitz-research/monkey](https://github.com/blitz-research/monkey)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.monkey` | [hello.monkey](hello.monkey) creato, verifiche pendenti |
| `.monkey2` | [hello.monkey2](variants/monkey2-f16dc421/hello.monkey2) creato, verifiche pendenti |
