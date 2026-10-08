# #526 Parrot

Voce canonica `Parrot`, tipo `programming`, language_id `278`.

Fornire un input originale al VM Parrot generico e stampare il saluto.

## Toolchain e riproduzione

Required genuine compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Parrot e frontend PASM. Il file .parrot è testo sorgente in formato assembly, selezionato esplicitamente con -a; non è bytecode inventato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
parrot -a hello.parrot
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Parrot è il VM comune alle voci PASM e PIR; questa voce generica usa la sua estensione canonica con una selezione del frontend. Toolchain assente, entrambi i flag pending.

Requisiti residui:

- Required parrot compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://parrot.github.io/html/docs/intro.pod.html](https://parrot.github.io/html/docs/intro.pod.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.parrot` | [hello.parrot](hello.parrot) creato, verifiche pendenti |
