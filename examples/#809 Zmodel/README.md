# #809 Zmodel

Voce canonica e ordine originali di reference/languages.yml.

Analizzare uno schema Zmodel con default del saluto.

## Toolchain e riproduzione

ZenStack 2.22.3; Prisma 6.19.0; Node.js 22.20.0; Python 3.13.9; SQLite 3.51.0. Prova eseguita su Windows x64. Le versioni effettive sono nel log.

Dalla cartella dell'esempio, installare dipendenze isolate e verificare:

```text
npm --prefix .tools install --save-exact zenstack@2.22.3 @zenstackhq/runtime@2.22.3; npm --prefix .tools-prisma install --save-exact prisma@6.19.0
python verify.py .tools .tools-prisma
```

## Stato ed evidenza

Artefatto creato; sintassi verificata; semantica verificata.

Il parser ufficiale ZenStack carica lo schema originale e il suo PrismaSchemaGenerator produce lo schema Prisma. Prisma 6 valida e genera SQL; SQLite inserisce una riga senza message e verifica il saluto predefinito. La policy allow non è esercitata tramite un client ORM. Dipendenze e risultati sono isolati dalla cartella del campione.

Risultato atteso: Hello, World!.

Log reale: [verification/result.json](verification/result.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Fonti primarie

- [https://github.com/zenstackhq/zenstack/tree/v2.22.3](https://github.com/zenstackhq/zenstack/tree/v2.22.3)
- [https://zenstack.dev/docs/reference/cli](https://zenstack.dev/docs/reference/cli)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.zmodel` | [hello.zmodel](hello.zmodel) sintassi e semantica verificate |
