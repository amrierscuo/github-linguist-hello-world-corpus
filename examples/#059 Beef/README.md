# #059 Beef

Voce canonica: `Beef`, tipo `programming`, `language_id: 545626333`.

Compilare un’applicazione console Beef e stampare Hello, World! da Program.Main.

## Toolchain e riproduzione

BeefBuild.exe — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede BeefBuild e la libreria System della stessa distribuzione. I file di workspace vanno generati con BeefBuild -new nella copia di lavoro; il corpus contiene il modulo sorgente originale.

Comando/procedura dalla directory dell’esempio:

```text
In una copia di lavoro: BeefBuild -new; sostituire src/Program.bf con il sorgente fornito; BeefBuild -run
```

Risultato atteso: Workspace compilato senza errori; console Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Usa la funzione main statica e Console.WriteLine della libreria Beef. BeefBuild non è presente: nessuna compilazione o esecuzione è attestata.

Requisiti residui:

- BeefBuild.exe toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://www.beeflang.org/docs/getting-start/](https://www.beeflang.org/docs/getting-start/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bf` | [Program.bf](src/Program.bf) creato, verifiche pendenti |
