# #611 Regular Expression

Voce canonica `Regular Expression`, tipo `data`, language_id `363378884`.

Compilare una regex Python che riconosce il saluto e cattura World.

## Toolchain e riproduzione

Python standard-library re regular expression engine — 3.13.9. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 re nativo; dialetto dichiarato con named group (?P<name>...).

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Fullmatch valido e controlli Reader/punteggiatura extra rifiutati dal motore reale.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.regexp` | [hello.regexp](hello.regexp) verificato |
| `.regex` | [hello.regex](variants/regex-b64e0ba7/hello.regex) creato, verifiche pendenti |
