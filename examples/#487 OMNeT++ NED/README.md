# #487 OMNeT++ NED

## Verified on November 18, 2026

The original definitions were used by the actual native OMNeT++ message generator and console simulator. The simulation produced the exact greeting.

Run `opp_makemake -f --deep -o hello; make MODE=release; ./hello -u Cmdenv -f omnetpp.ini --cmdenv-express-mode=false --cmdenv-log-level=info`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Generate the message and start an OMNeT++ network that records greeting.

## Toolchain

OMNeT++ 6.2 compatibile

## Procedure

opp_makemake -f --deep -o hello; make; ./hello -u Cmdenv -f omnetpp.ini

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The package includes MSG/NED, C++ module and original configuration; the goal uses the generated field of the message.

Remaining requirements:
- opp_msgtool, the NED compiler and the OMNeT++ libraries and runtime are not set up.

## Primary sources

- [https://doc.omnetpp.org/omnetpp/manual/](https://doc.omnetpp.org/omnetpp/manual/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ned` | [Hello.ned](Hello.ned) Syntax and behavior verified |

</details>
