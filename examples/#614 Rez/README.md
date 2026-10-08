# #614 Rez

Voce canonica `Rez`, tipo `programming`, language_id `498022874`.

Compilare una risorsa Mac Rez TEXT originale con il saluto nel payload.

## Toolchain e riproduzione

Required genuine Rez compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Apple Rez/DeRez e il template Types.r del SDK Mac compatibile.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Rez -i /path/to/MacSDK/RezHeaders hello.r -o build/hello.rsrc; DeRez -only TEXT build/hello.rsrc
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Resource id 128 e payload originali; toolchain Apple assente.

Requisiti residui:

- Required Rez compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Cpp/Resources/Resources.html](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Cpp/Resources/Resources.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.r` | [hello.r](hello.r) creato, verifiche pendenti |
