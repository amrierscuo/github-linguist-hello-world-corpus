# #760 WDL

Voce canonica `WDL`, tipo `programming`, language_id `374521672`.

The workflow performs the `hello` task, which writes the greeting on its stdout. `read_string(stdout())` reads the file and the workflow exposes `greeting.message` equal to `Hello, World!`.

## Toolchain and reproduction

miniwdl 1.15.0 original, Python 3.12.3 official backend udocker 1.3.17 with englib 1.2.11 and official image `ubuntu:20.04`. Try on Ubuntu 24.04 WSL2 x86_64, with ordinary Linux user.

Install the packages in a dedicated Python environment outside the corpus. Set `UDOCKER_DIR` and `UDOCKER_TMP` on dedicated workbooks.

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

## Status and evidence

Artefatto created, syntax verified, behavior verified.

The original miniwdl runner ends with exit code 0, returns `{"greeting.message": "Hello, World!"}` and the task produces exactly `Hello, World!` followed by newline, without stderr. The parsing/typecheck and the checker on the real results pass. `miniwdl check` reports the preexisting notice `NameCollision` for the `greeting` name; the

[Log runtime](verification/runtime.json) with timestamp UTC, versions, commands, exit code, output, runner logs, image digest and sorgenti/checker. hash The previous parsing test remains in [result.json](verification/result.json). The backend is officially included in miniwdl, classified BETA by documentation. The test certifies this minimal workflow in this minimum environment

## Primary sources

- [WDL specification](https://github.com/openwdl/wdl/blob/wdl-1.0/SPEC.md)
- [miniwdl originale](https://github.com/chanzuckerberg/miniwdl)
- [Backend ufficiali miniwdl, incluso udocker](https://miniwdl.readthedocs.io/en/latest/runner_backends.html)
- [udocker originale](https://github.com/indigo-dc/udocker)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.wdl` | [hello.wdl](hello.wdl) syntax and behavior verified |
