# #450 Move

Voce canonica `Move`, tipo `programming`, language_id `638334599`.

Costruire un modulo nel linguaggio Move originale e testare la funzione che restituisce una stringa.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede compiler/test runner move-language/move e la MoveStdlib indicata in Move.toml, con versione compatibile.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
move build; move test
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Modulo e test originali; toolchain Move non disponibile. Non è richiesto alcun account o deployment su blockchain.

Requisiti residui:

- Original Move compiler/test runner and matching stdlib are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/move-language/move](https://github.com/move-language/move)
- [https://move-language.github.io/move/strings.html](https://move-language.github.io/move/strings.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.move` | [greeting.move](sources/greeting.move) creato, verifiche pendenti |
