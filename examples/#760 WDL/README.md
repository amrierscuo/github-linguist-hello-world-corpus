# #760 WDL

Voce canonica `WDL`, tipo `programming`, language_id `374521672`.

Il workflow esegue il task `hello`, che scrive il saluto sul proprio stdout. `read_string(stdout())` legge il file e il workflow espone `greeting.message` uguale a `Hello, World!`.

## Toolchain e riproduzione

miniwdl 1.15.0 originale, Python 3.12.3, backend ufficiale udocker 1.3.17 con englib 1.2.11 e immagine ufficiale `ubuntu:20.04`. Prova su Ubuntu 24.04 WSL2 x86_64, con utente Linux ordinario.

Installare i package in un ambiente Python dedicato esterno al corpus. Impostare `UDOCKER_DIR` e `UDOCKER_TMP` su cartelle di lavoro dedicate. La prova registrata usa dipendenze Python, archivio delle immagini e directory del run isolati.

```sh
python3 -m venv /path/to/wdl-env
. /path/to/wdl-env/bin/activate
python3 -m pip install miniwdl==1.15.0 udocker==1.3.17
export UDOCKER_DIR=/path/to/wdl-work/udocker
export UDOCKER_TMP=/path/to/wdl-work/tmp
mkdir -p "$UDOCKER_DIR" "$UDOCKER_TMP"
udocker install
udocker pull ubuntu:20.04
python3 verify.py
miniwdl check hello.wdl
MINIWDL__SCHEDULER__CONTAINER_BACKEND=udocker MINIWDL__CALL_CACHE__GET=false MINIWDL__CALL_CACHE__PUT=false miniwdl run hello.wdl --dir /path/to/wdl-runs > /path/to/result.json
python3 verify_output.py /path/to/result.json
```

Sostituire i percorsi `/path/to` con le proprie cartelle di lavoro esterne al clone. Il primo comando richiede il supporto `venv` della propria installazione Python. Il checker finale confronta sia il valore del workflow sia stdout e stderr realmente prodotti dal task. udocker esegue il container in spazio utente e non richiede di avviare Docker o riconfigurare un daemon.

## Stato ed evidenza

Artefatto creato, sintassi verificata, semantica verificata.

Il runner miniwdl originale termina con exit code 0, restituisce `{"greeting.message": "Hello, World!"}` e il task produce esattamente `Hello, World!` seguito da newline, senza stderr. Il parsing/typecheck e il checker sui risultati reali passano. `miniwdl check` segnala l'avviso preesistente `NameCollision` per il nome `greeting`; l'esecuzione del workflow riesce.

[Log runtime](verification/runtime.json) con timestamp UTC, versioni, comandi, exit code, output, log del runner, digest dell'immagine e hash dei sorgenti/checker. La precedente prova di solo parsing rimane in [result.json](verification/result.json). Il backend è quello ufficialmente incluso in miniwdl, classificato BETA dalla documentazione. La prova certifica questo workflow minimo in questo ambiente.

## Fonti primarie

- [WDL specification](https://github.com/openwdl/wdl/blob/wdl-1.0/SPEC.md)
- [miniwdl originale](https://github.com/chanzuckerberg/miniwdl)
- [Backend ufficiali miniwdl, incluso udocker](https://miniwdl.readthedocs.io/en/latest/runner_backends.html)
- [udocker originale](https://github.com/indigo-dc/udocker)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.wdl` | [hello.wdl](hello.wdl) sintassi e semantica verificate |
