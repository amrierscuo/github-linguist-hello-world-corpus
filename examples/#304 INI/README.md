# #304 INI

Leggere message in una sezione INI greeting e recuperare il saluto.

## Toolchain

Python 3.13.9 stdlib configparser

## Comandi e procedura

python --version; python verify.py

## Risultato atteso

Sezione greeting e valore message corretti; stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Il parser stdlib è reale e strict=True; l’interpolazione è disabilitata perché non serve al file. verify.py controlla anche il nome della sezione.

Verifica effettiva del 2026-10-08T12:29:57.264907+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://docs.python.org/3/library/configparser.html](https://docs.python.org/3/library/configparser.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ini` | [hello.ini](hello.ini) verificato |
| `.cfg` | [hello.cfg](variants/cfg-9b787153/hello.cfg) creato, verifiche pendenti |
| `.cnf` | [hello.cnf](variants/cnf-a92aaf57/hello.cnf) creato, verifiche pendenti |
| `.container` | [hello.container](variants/container-f1a82e30/hello.container) creato, verifiche pendenti |
| `.dof` | [hello.dof](variants/dof-3be3c923/hello.dof) creato, verifiche pendenti |
| `.frm` | artefatto da generare L’estensione include descriptor MySQL di vista legacy e file tabella binari. Senza esportazione genuina da una versione compatibile del server non si inventano metadati interni come timestamp, checksum o SQL-mode. |
| `.lektorproject` | [hello.lektorproject](variants/lektorproject-74dbf384/hello.lektorproject) creato, verifiche pendenti |
| `.mount` | [tmp-corpus-hello.mount](variants/mount-c89a52c2/tmp-corpus-hello.mount) creato, verifiche pendenti |
| `.network` | [hello.network](variants/network-e59c1258/hello.network) creato, verifiche pendenti |
| `.prefs` | [hello.prefs](variants/prefs-3d6ae810/hello.prefs) creato, verifiche pendenti |
| `.pro` | [hello.pro](variants/pro-1d8a87ac/hello.pro) creato, verifiche pendenti |
| `.properties` | [hello.properties](variants/properties-4792f091/hello.properties) creato, verifiche pendenti |
| `.service` | [corpus-hello.service](variants/service-a434241b/corpus-hello.service) creato, verifiche pendenti |
| `.socket` | [corpus-hello.socket](variants/socket-342b56ef/corpus-hello.socket) creato, verifiche pendenti |
| `.target` | [corpus-hello.target](variants/target-459dc81b/corpus-hello.target) creato, verifiche pendenti |
| `.timer` | [corpus-hello.timer](variants/timer-fc779652/corpus-hello.timer) creato, verifiche pendenti |
| `.url` | [hello.url](variants/url-4058ac74/hello.url) creato, verifiche pendenti |
