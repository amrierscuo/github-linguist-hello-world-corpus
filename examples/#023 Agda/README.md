# #023 Agda

Voce canonica: `Agda`, tipo `programming`, `language_id: 12`.
`Hello.agda` definisce `main : IO ⊤` e invoca `putLine "Hello, World!"`.
Il postulate di I/O è collegato al backend GHC tramite le pragmas `FOREIGN` e
`COMPILE`; la conversione `Text.unpack` passa la stringa Agda a `putStrLn` Haskell.

## Toolchain e riproduzione

Toolchain richiesta: **Agda con backend GHC** e **GHC** con il pacchetto `text`.
La documentazione consultata è Agda 2.9.0; una versione locale funzionante deve
essere installata e registrata prima di attestare la verifica. Non serve la
standard library Agda: si importano soltanto moduli `Agda.Builtin`.
Dalla directory di questo esempio:

```powershell
agda --version
ghc --version
agda Hello.agda
agda --compile Hello.agda
./Hello.exe
```

Su sistemi Unix l'eseguibile generato si invoca come `./Hello`.
Risultato atteso: typecheck e compilazione senza errori; esecuzione con codice 0 e
una riga esattamente `Hello, World!`.

## Stato ed evidenza

Artefatto creato; sintassi **in attesa**; semantica **in attesa**.
Requisito mancante: gli eseguibili `agda` e `ghc` non sono disponibili nel PATH
dell'ambiente verificato. La revisione della struttura rispetto alla documentazione
non è conteggiata come typecheck. Il postulate è un confine FFI: solo la compilazione
GHC controlla il collegamento Haskell; il typecheck Agda da solo non prova l'effetto I/O.

Log: [environment.json](verification/environment.json), che registra soltanto
la disponibilità degli strumenti e SHA-256 del sorgente. I percorsi della macchina
sono normalizzati secondo `path_normalization`; nessuna esecuzione del linguaggio
è dichiarata.

## Fonti ufficiali

- [Backend GHC, compilazione e esempio di I/O](https://agda.readthedocs.io/en/latest/tools/compilers.html).
- [FFI, pragmas e mapping String verso Data.Text.Text](https://agda.readthedocs.io/en/latest/language/foreign-function-interface.html).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.agda` | [Hello.agda](Hello.agda) creato, verifiche pendenti |
