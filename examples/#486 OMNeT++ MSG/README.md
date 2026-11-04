# #486 OMNeT++ MSG

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
| `.msg` | [Greeting.msg](Greeting.msg) created; verification pending |
