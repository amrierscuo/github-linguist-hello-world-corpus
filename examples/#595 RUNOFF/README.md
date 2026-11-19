# #595 RUNOFF

## Verified on November 19, 2026

The historical compatible converter parsed the untouched DEC RUNOFF document and translated it to troff. The rendered page contains the greeting.

Run `rnotroff -n < hello.rno > hello.troff && groff -Tascii hello.troff`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Format a RUNOFF document containing greeting.

Canonical type `markup`, language_id `315`.

Provided Toolchain: Digital Standard Runoff or compatible implementation.

From the example directory:

```sh
RUNOFF hello.rno
```

Expected result: formatted document with Hello, World!.

A Markdown renderr does not verify the RUNOFF commands.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime RUNOFF storico non disponibile.

Sources:

- [RUNOFF manual DEC](https://bitsavers.org/pdf/dec/vax/vms/5.0/AA-LA51A-TE_VAX_DIGITAL_Standard_Runoff_Reference_Manual_Apr88.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rnh` | [hello.rnh](variants/rnh-1c39dfc9/hello.rnh) created; verification pending |
| `.rno` | [hello.rno](hello.rno) Syntax and behavior verified |

</details>
