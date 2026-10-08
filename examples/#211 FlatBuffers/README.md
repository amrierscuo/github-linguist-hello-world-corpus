# #211 FlatBuffers

Voce canonica `FlatBuffers`, tipo `data`, language_id `577640576`.

Definire lo schema FlatBuffers Greeting e codificare/decodificare un messaggio JSON con identificatore binario HELO.

## Toolchain e riproduzione

Official FlatBuffers flatc binary schema compiler and codec — flatc version 25.12.19. Ambiente della prova: **Windows x64**.

flatc ufficiale 25.12.19 portable Windows x64. Usare una cartella build separata; schema, JSON originale e log sono i soli artefatti inclusi.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
flatc --binary --strict-json -o build hello.fbs greeting.json; flatc --json --strict-json -o build hello.fbs -- build/greeting.bin
```

Risultato atteso: JSON decodificato {"message":"Hello, World!"}; identificatore HELO; exit 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova verifica il JSON decodificato esatto, il campo message e l’identificatore HELO ai byte 4..7 del vero FlatBuffer. L’hash del binario temporaneo è nel log.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://flatbuffers.dev/schema/](https://flatbuffers.dev/schema/)
- [https://flatbuffers.dev/flatc/](https://flatbuffers.dev/flatc/)
- [https://github.com/google/flatbuffers/releases](https://github.com/google/flatbuffers/releases)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fbs` | [hello.fbs](hello.fbs) verificato |
