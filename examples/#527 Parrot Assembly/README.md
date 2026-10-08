# #527 Parrot Assembly

Voce canonica `Parrot Assembly`, tipo `programming`, language_id `279`.

Eseguire istruzioni PASM che impostano il registro stringa e invocano print.

## Toolchain e riproduzione

Required genuine compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Parrot VM con frontend PASM.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
parrot hello.pasm
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente assembly originale; interpreter non configurato. L’estensione .pasm distingue l’assembly dalla voce generica e dal PIR.

Requisiti residui:

- Required parrot compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://parrot.github.io/html/docs/user/pasm/index.pod.html](https://parrot.github.io/html/docs/user/pasm/index.pod.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pasm` | [hello.pasm](hello.pasm) creato, verifiche pendenti |
