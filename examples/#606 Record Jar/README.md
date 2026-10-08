# #606 Record Jar

Voce canonica `Record Jar`, tipo `data`, language_id `865765202`.

Leggere un Record Jar originale nel formato del registry dei language subtags.

## Toolchain e riproduzione

Existing language_data authentic format parser — 1.4.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

language-data 1.4.0 e suo registry_parser.parse_file esistente.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Una fixture originale private-use qaa contiene Description Hello, World!. Non si presenta come copia autorevole IANA. Il parser reale decodifica header, separatore e record, confrontati dal helper.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.rfc-editor.org/rfc/rfc5646#section-3.1.1](https://www.rfc-editor.org/rfc/rfc5646#section-3.1.1)
