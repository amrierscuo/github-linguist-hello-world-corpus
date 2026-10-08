# #068 BitBake

Voce canonica: `BitBake`, tipo `programming`, language_id `32`.

Eseguire una ricetta BitBake originale con un task Python do_build che emette Hello, World!.

## Toolchain e riproduzione

BitBake upstream branch 2.10, versione dichiarata dal runtime 2.9.1; Python 3.12.3.

BitBake e Python 3 nel PATH; eseguire in una copia temporanea su filesystem Linux che supporti socket Unix. Serve en_US.UTF-8. Per una locale privata: localedef --no-archive -i en_US -f UTF-8 <locale>/en_US.UTF-8; esportare LOCPATH=<locale>, LC_ALL=en_US.UTF-8 e BB_ENV_PASSTHROUGH_ADDITIONS="LOCPATH LANG LC_ALL".

Comandi dalla directory dell’esempio; `<output>` indica una directory temporanea esterna al corpus.

```text
Da build/: BBPATH="$PWD" bitbake -p
Da build/: BBPATH="$PWD" bitbake hello
```

Risultato atteso: 1 ricetta analizzata, 0 errori; task do_build riuscito e riga Hello, World! nel log.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser e il task Python reali hanno completato la prova. Corretto il config minimo: PN viene derivata dal filename tramite bb.parse.vars_from_file. Ambiente temporaneo su filesystem Linux, locale en_US.UTF-8 generata senza cambiare le locale di sistema; LOCPATH passato anche al server con BB_ENV_PASSTHROUGH_ADDITIONS. Il warning LAYERSERIES_COMPAT del layer standalone rimane registrato e non impedisce il task. Server isolato arrestato.

Prova reale: [finish.json](verification/finish.json), con UTC, comandi, versioni, exit code, stdout/stderr e SHA-256 dei sorgenti. Le sostituzioni dei percorsi sono documentate nel log. I prodotti di compilazione e le dipendenze rimangono nelle directory di lavoro.

## Fonti primarie

- https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html
- https://github.com/openembedded/bitbake/tree/2.10

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.bb` | [hello_1.0.bb](meta-hello/hello_1.0.bb), [hello_1.0.bb](variants/ext-bbappend-2e6262617070656e64/hello_1.0.bb), [hello_1.0.bb](variants/ext-inc-2e696e63/hello_1.0.bb) sintassi e semantica verificate |
| `.bbappend` | [hello_1.0.bbappend](variants/ext-bbappend-2e6262617070656e64/hello_1.0.bbappend) sintassi e semantica verificate |
| `.bbclass` | [base.bbclass](meta-hello/classes/base.bbclass) sintassi e semantica verificate |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) sintassi e semantica verificate |
