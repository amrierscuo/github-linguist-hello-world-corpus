# #620 Robots Exclusion Rules

Voce canonica `Robots Exclusion Rules`, tipo `data`, language_id `674736065`.

Verificare una policy robots.txt che ammette il file del saluto e blocca un percorso privato.

## Toolchain e riproduzione

Python standard-library urllib.robotparser policy engine — 3.13.9. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

urllib.robotparser Python standard library; file e target locale originali.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser reale ammette /hello.txt e rifiuta /private/file per CorpusBot. Il target contiene il saluto; nessun accesso di rete e nessun hosting.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.rfc-editor.org/rfc/rfc9309](https://www.rfc-editor.org/rfc/rfc9309)
