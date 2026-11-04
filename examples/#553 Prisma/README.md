# #553 Prisma

Voce canonica e ordine originali di reference/languages.yml.

Validare Prisma Schema Language con modello Greeting e default Hello, World!.

## Toolchain and reproduction

Prisma 7.10.0; Node.js 22.20.0; Python 3.13.9; SQLite 3.51.0. Test performed on Windows x64.

From the example folder, install isolated dependencies and check:

```text
npm --prefix .tools install --save-exact prisma@7.10.0
python verify.py .tools
```

## Status and evidence

Artefatto created; syntax verified; behavior verified.

Prisma valida lo schema originale e genera la migrazione SQL con migrate diff. SQLite esegue il SQL e inserisce una riga omettendo text: il valore letto deve essere Hello, World!. Config e database sono locali temporanei. Non viene dichiarata una prova del Prisma Client.

Expected result: Hello, World!.

Log reale: [verification/toolchain.json](verification/toolchain.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Primary sources

- [https://docs.prisma.io/docs/cli/v7/migrate/diff](https://docs.prisma.io/docs/cli/v7/migrate/diff)
- [https://www.prisma.io/docs/orm/prisma-schema/data-model/models](https://www.prisma.io/docs/orm/prisma-schema/data-model/models)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.prisma` | [hello.prisma](hello.prisma) syntax and behavior verified |
