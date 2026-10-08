# #619 RobotFramework

Voce canonica `RobotFramework`, tipo `programming`, language_id `324`.

Eseguire un test Robot Framework originale che costruisce e confronta il saluto.

## Toolchain e riproduzione

Official Robot Framework test parser and execution engine — Robot Framework 7.5 (Python 3.13.9 on win32). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Robot Framework ufficiale 7.5 e Python 3.13.9.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python -m robot --outputdir build --log NONE --report NONE hello.robot
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Parser e runner reali, test Should Be Equal passato e Log To Console osservato; output XML con SHA nel log.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.robot` | [hello.robot](hello.robot), [main.robot](variants/resource-78a02e24/main.robot) creato, verifiche pendenti |
| `.resource` | [hello.resource](variants/resource-78a02e24/hello.resource) creato, verifiche pendenti |
