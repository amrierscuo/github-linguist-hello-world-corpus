# #322 JCL

Copy a Hello, World! line from in-stream data to spool SYSOUT with IEBGENER.

Canonical type `programming`, language_id `316620079`.

Suggested toolchain: IBM z/OS JES and IEBGENER utilities.

From the example directory:

```sh
Sottoporre hello.jcl a JES in una coda di prova e leggere SYSUT2.
```

Expected result: step COPY with RC 0; SYSUT2 contains Hello, World!.

The JOB card is illustrated: ACCT, CLASS and MSGCLASS depend on the installation. No job has been performed on a mainframe.

Stato iniziale: creato; sintassi e semantica in attesa. Ambiente IBM z/OS JES non disponibile.

Sources:

- [IBM — IEBGENER](https://www.ibm.com/docs/en/zos/3.1.0?topic=utilities-iebgener-sequential-copygenerate-data-set-program)
- [IBM — dati in-stream JCL](https://www.ibm.com/docs/en/zos/3.1.0?topic=statement-dd-data)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jcl` | [hello.jcl](hello.jcl) created; verification pending |
