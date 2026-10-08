# #047 Avro IDL

Voce canonica: `Avro IDL`, tipo `data`, `language_id: 785497837`.

Compilare un record Avro IDL con default Hello, World!, leggere il default e conservare il saluto durante encode/decode binario Avro.

## Toolchain e riproduzione

Official Apache Avro tools and core Java APIs — 1.12.0. Ambiente della prova: **Windows x64**.

Scaricare avro-tools-1.12.0.jar dal Maven Central ufficiale in .tools; usare un JDK per il lancio del sorgente Java. Prova locale: Microsoft OpenJDK 21.0.12.1.

Comando/procedura dalla directory dell’esempio:

```text
java -jar .tools/avro-tools-1.12.0.jar idl hello.avdl hello.avpr; java --class-path .tools/avro-tools-1.12.0.jar AvroCheck.java hello.avpr
```

Risultato atteso: Exit 0; Hello, World!; PASS: compiled IDL default; genuine Avro binary encode/decode.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

AvroCheck.java delega parsing del protocollo, accesso al default e serializzazione a org.apache.avro; non implementa un parser Avro. Il protocollo generato e i dati binari sono prodotti di verifica in work.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://avro.apache.org/docs/1.12.0/idl-language/](https://avro.apache.org/docs/1.12.0/idl-language/)
- [https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/generic/GenericData.html](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/generic/GenericData.html)
- [https://repo.maven.apache.org/maven2/org/apache/avro/avro-tools/1.12.0/](https://repo.maven.apache.org/maven2/org/apache/avro/avro-tools/1.12.0/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.avdl` | [hello.avdl](hello.avdl) verificato |
