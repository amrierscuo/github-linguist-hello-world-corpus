# #322 JCL

## Verified on November 19, 2026

The guest executed HELLO with SYSUT2 routed to the configured class Z line printer. The native job boundaries in the changed printer output enclosed the exact greeting.

Run `Boot the isolated Turnkey 5 guest using the recorded Hercules script, submit hello.jcl and read prt/prt00f.txt`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

[Prior attempt](verification/native_20261119_wave800_prior_attempt.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.jcl` | [hello.jcl](hello.jcl) Syntax and behavior verified |

</details>
