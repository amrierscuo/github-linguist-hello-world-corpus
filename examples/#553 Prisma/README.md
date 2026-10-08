# #553 Prisma

Voce canonica e ordine originali di reference/languages.yml.

Validare Prisma Schema Language con modello Greeting e default Hello, World!.

## Toolchain e riproduzione

Prisma 7.10.0; Node.js 22.20.0; Python 3.13.9; SQLite 3.51.0. Prova eseguita su Windows x64. Le versioni effettive sono nel log.

Dalla cartella dell'esempio, installare dipendenze isolate e verificare:

```text
npm --prefix .tools install --save-exact prisma@7.10.0
python verify.py .tools
```

## Stato ed evidenza

Artefatto creato; sintassi verificata; semantica verificata.

Prisma valida lo schema originale e genera la migrazione SQL con migrate diff. SQLite esegue il SQL e inserisce una riga omettendo text: il valore letto deve essere Hello, World!. Config e database sono locali temporanei. Non viene dichiarata una prova del Prisma Client.

Risultato atteso: Hello, World!.

Log reale: [verification/toolchain.json](verification/toolchain.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Fonti primarie

- [https://docs.prisma.io/docs/cli/v7/migrate/diff](https://docs.prisma.io/docs/cli/v7/migrate/diff)
- [https://www.prisma.io/docs/orm/prisma-schema/data-model/models](https://www.prisma.io/docs/orm/prisma-schema/data-model/models)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.prisma` | [hello.prisma](hello.prisma) sintassi e semantica verificate |
