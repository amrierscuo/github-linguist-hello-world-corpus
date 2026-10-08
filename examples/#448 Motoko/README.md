# #448 Motoko

Voce canonica `Motoko`, tipo `programming`, language_id `202937027`.

Eseguire una query Motoko di un actor locale e controllare una seconda stringa parametro.

## Toolchain e riproduzione

Authentic Motoko compiler and actor interpreter via official-linked Node bindings — node-motoko 5.0.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler Motoko autentico attraverso il binding Node citato dal progetto ufficiale; la versione realmente usata è nel log.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools motoko; node verify.cjs .tools
```

Risultato atteso: Il risultato Motoko contiene "Hello, World!" : Text; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

mo.check verifica il tipo, mo.run esegue l’actor e la query, e l’assert Reader controlla il parametro. Ambito: interprete locale, senza deployment di canister.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.internetcomputer.org/languages/motoko/reference/compiler-ref/](https://docs.internetcomputer.org/languages/motoko/reference/compiler-ref/)
- [https://github.com/caffeinelabs/motoko](https://github.com/caffeinelabs/motoko)
- [https://github.com/caffeinelabs/node-motoko](https://github.com/caffeinelabs/node-motoko)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mo` | [hello.mo](hello.mo) verificato |
