# #127 Clue

Voce canonica: `Clue`, tipo `programming`, `language_id: 163763508`.

Compilare il sorgente Clue in Lua ed eseguirlo nell’interprete embedded ufficiale per stampare il saluto.

## Toolchain e riproduzione

Official Clue native compiler and embedded Lua interpreter — clue 3.4.7. Ambiente della prova: **Windows x64**.

Distribuzione portable ufficiale Clue 3.4.7 Windows x64 dal repository ClueLang/Clue. --dontsave evita di creare il Lua generato nella cartella dell’esempio; --execute usa la feature interpreter incorporata.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
clue --dontsave --execute hello.clue
```

Risultato atteso: Exit 0; banner del compilatore più una riga Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Questo è Clue di ClueLang, con concatenamento Lua .. e sintassi C/Rust; local e print sono compilati veramente. Il log mostra compilazione ed esecuzione e registra SHA-256 del binario ufficiale.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://github.com/ClueLang/Clue](https://github.com/ClueLang/Clue)
- [https://github.com/ClueLang/Clue/wiki](https://github.com/ClueLang/Clue/wiki)
- [https://github.com/ClueLang/Clue/releases/tag/v3.4.7](https://github.com/ClueLang/Clue/releases/tag/v3.4.7)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.clue` | [hello.clue](hello.clue) verificato |
