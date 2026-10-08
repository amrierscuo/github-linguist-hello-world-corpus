# #522 POV-Ray SDL

Voce canonica `POV-Ray SDL`, tipo `programming`, language_id `275`.

Valutare una stringa SDL e renderizzare una piccola scena POV-Ray originale.

## Toolchain e riproduzione

Original POV-Ray SDL parser and renderer — POV-Ray 3.7.0.10 Ubuntu 3build4. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

POV-Ray 3.7.0.10 ufficiale, librerie SDL/runtime locali.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
povray +Ihello.pov +Obuild/hello.png +W16 +H16 -D +FN
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il saluto è una direttiva #debug realmente valutata, oltre alla scena sphere/camera/light; non è un commento.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.povray.org/documentation/](https://www.povray.org/documentation/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pov` | [hello.pov](hello.pov), [driver.pov](variants/inc-dd126fb7/driver.pov) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
