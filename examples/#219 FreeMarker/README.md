# #219 FreeMarker

Voce canonica `FreeMarker`, tipo `programming`, language_id `115`.

Caricare un template Apache FreeMarker, interpolare name e verificare il rendering per World e Reader.

## Toolchain e riproduzione

Official Apache FreeMarker template parser and engine — 2.3.34. Ambiente della prova: **Windows x64**.

Apache FreeMarker 2.3.34 ufficiale da Maven Central e JDK 21. Collocare il JAR in .tools fuori dal deliverable; il Java helper usa le API ufficiali Configuration e Template.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java --class-path .tools/freemarker-2.3.34.jar FreeMarkerCheck.java .
```

Risultato atteso: Hello, World! e PASS del controllo parametrico.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Questa .ftl è un template FreeMarker. Il confronto controlla il contenuto esatto e newline per due valori, dopo il vero parsing del motore.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://freemarker.apache.org/docs/dgui_quickstart_basics.html](https://freemarker.apache.org/docs/dgui_quickstart_basics.html)
- [https://freemarker.apache.org/docs/pgui_quickstart_all.html](https://freemarker.apache.org/docs/pgui_quickstart_all.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ftl` | [hello.ftl](hello.ftl) verificato |
| `.ftlh` | [hello.ftlh](variants/ext-ftlh-2e66746c68/hello.ftlh) creato, verifiche pendenti |
