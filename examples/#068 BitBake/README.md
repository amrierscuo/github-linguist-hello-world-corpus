# #068 BitBake

Voce canonica: `BitBake`, tipo `programming`, language_id `32`.

Perform an original BitBake recipe with a Python do_build task that issues Hello, World!.

## Toolchain and reproduction

BitBake upstream branch 2.10, version declared by the 2.9.1 runtime; Python 3.12.3.

Put BitBake and Python 3 on PATH and run in a temporary copy on a Linux filesystem that supports Unix sockets. en_US.UTF-8 is required. To generate a private locale: localedef --no-archive -i en_US -f UTF-8 <locale>/en_US.UTF-8; export LOCPATH=<locale>, LC_ALL=en_US.UTF-8 and BB_ENV_PASSTHROUGH_ADDITIONS="LOCPATH LANG LC_ALL".

Commands from the directory of the example; `<output>` indicates a temporary directory external to the corpus.

```text
Da build/: BBPATH="$PWD" bitbake -p
Da build/: BBPATH="$PWD" bitbake hello
```

Expected result: 1 analyzed recipe, 0 errors; task do_build successful and row Hello, World! in the log.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The native parser and Python task completed the check. The minimal configuration was corrected: bb.parse.vars_from_file derives PN from the filename. The temporary environment used a Linux filesystem. The en_US.UTF-8 locale was generated without changing system locales; LOCPATH was passed to the server with BB_ENV_PASSTHROUGH_ADDITIONS. The standalone layer's LAYERSERIES_COMPAT warning was recorded and did not block the task. The isolated server was stopped.

Real test: [finish.json](verification/finish.json), with UTC, commands, versions, exit code, stdout/stderr and SHA-256 of sources.

## Primary sources

- https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html
- https://github.com/openembedded/bitbake/tree/2.10

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.bb` | [hello_1.0.bb](meta-hello/hello_1.0.bb), [hello_1.0.bb](variants/ext-bbappend-2e6262617070656e64/hello_1.0.bb), [hello_1.0.bb](variants/ext-inc-2e696e63/hello_1.0.bb) syntax and behavior verified |
| `.bbappend` | [hello_1.0.bbappend](variants/ext-bbappend-2e6262617070656e64/hello_1.0.bbappend) syntax and behavior verified |
| `.bbclass` | [base.bbclass](meta-hello/classes/base.bbclass) syntax and behavior verified |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) syntax and behavior verified |
