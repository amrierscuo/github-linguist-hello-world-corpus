# #523 Pact

Voce canonica `Pact`, tipo `programming`, language_id `756774415`.

Valutare un binding e format del linguaggio Pact Kadena nel REPL locale.

## Toolchain e riproduzione

Required genuine compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede l’interprete Pact di kadena-io/pact, con la funzione REPL print.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
pact; (load "hello.pact")
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente Pact originale; toolchain assente. Questa voce indica il linguaggio smart contract Kadena. Nessun deployment o account necessario.

Requisiti residui:

- Required pact compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pact-language.readthedocs.io/en/latest/pact-functions.html](https://pact-language.readthedocs.io/en/latest/pact-functions.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pact` | [hello.pact](hello.pact) creato, verifiche pendenti |
